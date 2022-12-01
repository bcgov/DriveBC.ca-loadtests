import React, { useRef, useEffect, useState } from 'react';
import { useDrop } from 'react-dnd';

import { feature, featureCollection, point } from '@turf/helpers';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

import Advisory from './Advisory.js';
import Layers from './Layers.js';
import Routes from './Routes.js';
import osm from './styles/osm.js';
import mt from './styles/maptiler.js';
import { getEvents } from './data/events.js';
import { getWebcams } from './data/webcams.js';
import { getAdvisories } from './data/advisories.js';
import videoIcon from '../assets/video-solid.png';
import eventIcon from '../assets/exclamation-triangle-solid.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLocationArrow, faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';

import './Map.css';
let start, end;


export default function Map(){
  const mapContainer = useRef(null);
  const map = useRef(null);
  const lng = -120.7862;
  const lat = 50.113;
  const zoom = 7.5;
  const location = new maplibregl.Marker().setLngLat([lng, lat])
  const start = new maplibregl.Marker({color: '#003399', draggable: true});
  const end = new maplibregl.Marker({color: '#009933', draggable: true});
  const [layersOpen, setLayersOpen] = useState(false);
  const [routesOpen, setRoutesOpen] = useState(false);
  const [advisories, setAdvisories] = useState([]);

  const [{ isOver }, drop] = useDrop(
    () => ({
      accept: 'pin',
      drop: (item, monitor) => {
        const { x, y } = monitor.getClientOffset();
        const { lat, lng } = map.current.unproject([x, y - 48]);
        if (item.role === 'start') {
          start.setLngLat([lng, lat]).addTo(map.current);
        } else {
          end.setLngLat([lng, lat]).addTo(map.current);
        }
      }
    }),
    []
  );

  useEffect(() => {
    if (map.current) return; //stops map from intializing more than once
    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: 'https://api.maptiler.com/maps/streets-v2/style.json?key=AITV1LUU17CaN7lfvmfi',
      center: [lng, lat],
      zoom: zoom,
      maxZoom: 17,
      minZoom: 1,
    });
    location.addTo(map.current);
    start.remove();
    end.remove();
    window.map = map.current;
    window.start = start;
    window.end = end;

    map.current.on('load', async () => {
      const campoints = await getWebcams();
      const evpoints = await getEvents();

      map.current.loadImage(videoIcon, (error, image) => {
        if (error) throw error;
        map.current.addImage('video', image);
        map.current.addSource('webcams-points', { type: 'geojson', data: featureCollection(campoints) });
        map.current.addLayer({
          'id': 'webcams',
          'type': 'symbol',
          'source': 'webcams-points',
          'layout': {
            'icon-image': 'video',
          }
        });
      });

      map.current.loadImage(eventIcon, (error, image) => {
        if (error) throw error;
        map.current.addImage('event', image);
        map.current.addSource('events-points', { type: 'geojson', data: featureCollection(evpoints) });
        map.current.addLayer({
          'id': 'events',
          'type': 'symbol',
          'source': 'events-points',
          'layout': {
            'icon-image': 'event',
          }
        });
      });

      map.current.addSource('routed',
        {
          type: 'geojson',
          data: {
            type: "Feature",
            properties: {},
            geometry: {
              "type": "LineString",
              "coordinates": []
            }
          },
        },
      );

      map.current.addLayer({
        'id': 'route',
        'type': 'line',
        'source': 'routed',
        'paint': {
          'line-color': '#004eff',
          'line-width': 8,
        }
      });

      map.current.on('click', 'webcams', (e) => {
        const cam = e.features[0].properties;
        new maplibregl.Popup({
          maxWidth: '320px'
        }).setLngLat(e.lngLat)
          .setHTML(`
            <div>
              <h4>${cam.name}</h4>
              <img src="${cam.url}" width='300'>
              <p>${cam.caption}</p>
            </div>`
          )
          .addTo(map.current);
      });

      map.current.on('click', 'events', (e) => {
        const event = e.features[0].properties;
        new maplibregl.Popup({
          maxWidth: '320px'
        }).setLngLat(e.lngLat)
          .setHTML(`
            <div style='text-align: left'>
              <h4>${event.headline}</h4>
              <p>${event.description}</p>
            </div>`
          )
          .addTo(map.current);
      });

      let interval = setInterval(async() => {
        const travalad = await getAdvisories();
        setAdvisories(travalad);
      }, 10000);
    })

  });

  function zoomIn() {
    if (!map.current) { return; }
    map.current.setZoom(map.current.getZoom() + 0.5);
  }

  function zoomOut() {
    if (!map.current) { return; }
    map.current.setZoom(map.current.getZoom() - 0.5);
  }

  function myLocation() {
    if (!map.current) { return; }
    navigator.geolocation.getCurrentPosition(position => {
      const pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      };
      map.current.setZoom(14);
      map.current.setCenter(pos);
    });

  }

  function toggleLayers(openLayers) {
    setLayersOpen(openLayers);
    if (openLayers) { setRoutesOpen(false); }
  }

  function toggleRoutes(openRoutes) {
    setRoutesOpen(openRoutes);
    if (openRoutes) { setLayersOpen(false); }
  }

  function setStartToLocation() {
    if (!map.current) { return; }
    navigator.geolocation.getCurrentPosition(position => {
      const pos = [
        position.coords.longitude,
        position.coords.latitude
      ];
      map.current.setZoom(12);
      map.current.setCenter(pos);
      window.start.setLngLat(pos).addTo(map.current);
    });

  }

  function toggleLayer(layer, showLayer) {
    map.current.setLayoutProperty(layer, 'visibility', showLayer ? 'visible' : 'none');
  }

  function routeHandler(email) {
    if (!window.start.getLngLat() || !window.end.getLngLat()) {
      console.log('start or end not set');
      console.log(start.getLngLat());
      console.log(end.getLngLat());
      return;
    }

    if (!email) {
      email = 'test@oxd.com';
    }

    fetch('http://localhost:8000/api/routes/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email,
        name: "Primary route",
        start_location: window.start.getLngLat(),
        destination: window.end.getLngLat(),
      })
    }).then((response) => {
      if (response.status == 201) {
        return response.json()
      }
    }).then((data) => { console.log(data); if (data) { map.current.getSource('routed').setData(data) } })
      .catch((err) => console.log(err));
  }

  return (
    <div className="map-wrap" style={{ opacity: isOver ? 0.5 : 1 }} ref={drop}>
      <div ref={mapContainer} className="map" />

      <div className="map-control">
        <button className="my-location BC-Gov-SecondaryButton" onClick={myLocation}>
          <FontAwesomeIcon icon={faLocationArrow} />
        </button>
        <button className="zoom-in BC-Gov-SecondaryButton" onClick={zoomIn}>
          <FontAwesomeIcon icon={faPlus} />
        </button>
        <button className="zoom-out BC-Gov-SecondaryButton" onClick={zoomOut}>
          <FontAwesomeIcon icon={faMinus} />
        </button>
      </div>

      <Routes
        open={routesOpen}
        setRoutesOpen={toggleRoutes}
        setStartToLocation={setStartToLocation}
        routeHandler={routeHandler}
      />

      <Layers
        open={layersOpen}
        setLayersOpen={toggleLayers}
        toggleLayer={toggleLayer}
      />

      {advisories.length > 0 ? <Advisory advisories={advisories} />: null}

    </div>
  );
}
