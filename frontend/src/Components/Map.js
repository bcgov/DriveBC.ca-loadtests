import React, { useRef, useEffect, useState } from 'react';
import { useDrop } from 'react-dnd';

import { feature, featureCollection, point } from '@turf/helpers';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

import Layers from './Layers.js';
import Routes from './Routes.js';
import osm from './styles/osm.js';
import { getEvents } from './data/events.js';
import { getWebcams } from './data/webcams.js';

import './Map.css';


export default function Map(){
  const mapContainer = useRef(null);
  const map = useRef(null);
  const location = new maplibregl.Marker().setLngLat([-123.1207, 49.2827])
  const start = new maplibregl.Marker({color: '#003399', draggable: true});
  const end = new maplibregl.Marker({color: '#009933', draggable: true});
  const lng = -120.7862;
  const lat = 50.113;
  const zoom = 7.5;
  const [layersOpen, setLayersOpen] = useState(false);
  const [routesOpen, setRoutesOpen] = useState(true);

  const [{ isOver }, drop] = useDrop(
    () => ({
      accept: 'pin',
      drop: (item, monitor) => {
        const { x, y } = monitor.getClientOffset();
        const { lat, lng } = map.current.unproject([x, y - 48]);
        const pin = item.role === 'start' ? start : end;
        pin.setLngLat([lng, lat]).addTo(map.current);
      }
    }),
    []
  )

  useEffect(() => {
    if (map.current) return; //stops map from intializing more than once
    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: osm,
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
      console.log(evpoints);
      map.current.addSource('webcams-points', { type: 'geojson', data: featureCollection(campoints) });
      map.current.addSource('events-points', { type: 'geojson', data: featureCollection(evpoints) });
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
        'id': 'webcams',
        'type': 'circle',
        'source': 'webcams-points',
        'paint': {
          'circle-radius': 6,
          'circle-color': '#000099'
        }
      });

      map.current.addLayer({
        'id': 'events',
        'type': 'circle',
        'source': 'events-points',
        'paint': {
          'circle-radius': 10,
          'circle-color': '#FFFF00'
        }
      });

      map.current.addLayer({
        'id': 'route',
        'type': 'line',
        'source': 'routed',
        'paint': {
          'line-color': '#CC3300',
          'line-width': 10,
        }
      });
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
    map.current.setZoom(14);
    map.current.setCenter({ lng, lat });
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
    start.setLngLat([lng, lat]).addTo(map.current);
  }

  function toggleLayer(layer, showLayer) {
    map.current.setLayoutProperty(layer, 'visibility', showLayer ? 'visible' : 'none');
  }

  function routeHandler() {
    if (!start.getLngLat() || !end.getLngLat()) {
      console.log('start or end not set');
      return;
    }

    fetch('http://localhost:8000/api/routes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: "test@oxd.com",
        name: "Primary route",
        start_location: start.getLngLat(),
        destination: end.getLngLat(),
      })
    }).then((response) => response.json())
      .then((data) => {
        map.current.getSource('routed').setData(data);
      })
  }

  return (
    <div className="map-wrap" style={{ opacity: isOver ? 0.5 : 1 }} ref={drop}>
      <div ref={mapContainer} className="map" />

      <button className="my-location" onClick={myLocation}>&gt;</button>
      <button className="zoom-in" onClick={zoomIn}>+</button>
      <button className="zoom-out" onClick={zoomOut}>-</button>

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
    </div>
  );
}
