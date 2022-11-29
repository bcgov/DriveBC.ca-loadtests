import React, { useRef, useEffect, useState } from 'react';
import { useDrop } from 'react-dnd';

import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
import './Map.css';
import osm from './styles/osm.js';
import Layers from './Layers.js';
import Routes from './Routes.js';


export default function Map(){
  const mapContainer = useRef(null);
  const map = useRef(null);
  const location = new maplibregl.Marker().setLngLat([-123.1207, 49.2827])
  const start = new maplibregl.Marker({color: '#003399', draggable: true});
  const end = new maplibregl.Marker({color: '#009933', draggable: true});
  const [lng] = useState(-123.1207);
  const [lat] = useState(49.2827);
  const [zoom] = useState(14); 
  const [layersOpen, setLayersOpen] = useState(false);
  const [routesOpen, setRoutesOpen] = useState(true);

  const [{ isOver, canDrop }, drop] = useDrop(
    () => ({
      accept: 'pin',
      drop: (item, monitor) => {
        const { x, y } = monitor.getClientOffset();
        const { lat, lng } = map.current.unproject([x, y - 48]);
        const pin = item.role === 'start' ? start : end;
        pin.setLngLat([lng, lat]).addTo(map.current);
        console.log(monitor.getSourceClientOffset());
        console.log(monitor.getInitialSourceClientOffset());
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
      minZoom: 7,
    });
    location.addTo(map.current);
    start.remove();
    end.remove();
    window.map = map.current;
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

  return (
    <div className="map-wrap" style={{ opacity: isOver ? 0.5 : 1 }} ref={drop}>
      <div ref={mapContainer} className="map" />
      <Routes 
        open={routesOpen} 
        setRoutesOpen={toggleRoutes} 
        setStartToLocation={setStartToLocation} 
      />
      <Layers open={layersOpen} setLayersOpen={toggleLayers} />
      <button className="my-location" onClick={myLocation}>&gt;</button>
      <button className="zoom-in" onClick={zoomIn}>+</button>
      <button className="zoom-out" onClick={zoomOut}>-</button>
    </div>
  );
}
