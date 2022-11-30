import React, { useRef, useEffect, useState } from 'react';
import { useDrop } from 'react-dnd';

import { featureCollection, point } from '@turf/helpers';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

import Layers from './Layers.js';
import Routes from './Routes.js';
import osm from './styles/osm.js';
import Events from './data/events.js';
import Webcams from './data/webcams.js';

import './Map.css';


const webcamPoints = Webcams.map((webcam) => {
  const lng = webcam.location.longitude;
  const lat = webcam.location.latitude;

  return point([lng, lat], {
      url: webcam.links.currentImage,
      id: webcam.id,
      name: webcam.camName,
      caption: webcam.caption,
      coords: { lng, lat },
  }, { id: webcam.id })
})
const webcamsGeoJson = featureCollection(webcamPoints);

const eventsPoints = Events.map((event) => {
  const [lng, lat] = event.geography.coordinates[0];

  return point([lng, lat], {
      url: event.url,
      id: event.id,
      name: event.headline,
      caption: event.severity,
      coords: { lng, lat },
  }, { id: event.id })
})
const eventsGeoJson = featureCollection(eventsPoints);

export default function Map(){
  const mapContainer = useRef(null);
  const map = useRef(null);
  const location = new maplibregl.Marker().setLngLat([-123.1207, 49.2827])
  const start = new maplibregl.Marker({color: '#003399', draggable: true});
  const end = new maplibregl.Marker({color: '#009933', draggable: true});
  const lng = -123.1207;
  const lat = 49.2827;
  const zoom = 14; 
  const [layersOpen, setLayersOpen] = useState(true);
  const [routesOpen, setRoutesOpen] = useState(false);
  const [webcamsVisible, setWebcamVisilibity] = useState(true);

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

    map.current.on('load', () => {
      map.current.addSource('webcams-points', { type: 'geojson', data: webcamsGeoJson });
      map.current.addSource('events-points', { type: 'geojson', data: eventsGeoJson });
      map.current.addLayer({
        'id': 'webcams',
        'type': 'circle',
        'source': 'webcams-points',
        'paint': {
          'circle-radius': 10,
          'circle-color': '#FF0000'
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
      />

      <Layers 
        open={layersOpen} 
        setLayersOpen={toggleLayers} 
        toggleLayer={toggleLayer}
      />
    </div>
  );
}
