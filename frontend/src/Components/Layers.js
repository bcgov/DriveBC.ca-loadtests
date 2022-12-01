import React from 'react';

import videoIcon from '../assets/video-solid.png';
import eventIcon from '../assets/exclamation-triangle-solid.png';
import map from '../assets/map.png';
import terrain from '../assets/terrain.png';
import './Layers.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLayerGroup, faXmark } from '@fortawesome/free-solid-svg-icons';


export default function Layers({ open, setLayersOpen, toggleLayer}) {

  if (!open) {
    return (
      <button className="open-layers BC-Gov-SecondaryButton"
        onClick={() => setLayersOpen(true)}
      >
        <FontAwesomeIcon icon={faLayerGroup} />
      </button>
    )
  }

  return (
    <div className="layers">
      <button className="close-layers"
        onClick={() => setLayersOpen(false)}
      ><FontAwesomeIcon icon={faXmark} /></button>

      <h3>Base Layers</h3>

      <div className="layers-select">
        <div className="panel">
          <img className='map-image' src={map} alt="Map" />
          <div>Map</div>
        </div>

        <div className="panel">
          <img className='map-image' src={terrain} alt="Terrain" />
          <div>Terrain</div>
        </div>
      </div>

      <h3>Features</h3>

      <div>
        <img className="map-icon" src={videoIcon} alt="Webcam Icon" />
        <input
          type="checkbox"
          onChange={(e) => toggleLayer('webcams', e.target.checked)}
          defaultChecked
        /> Webcam
      </div>

      <div>
      <img className="map-icon" src={eventIcon} alt="Event Icon" />
        <input type="checkbox"
          onChange={(e) => toggleLayer('events', e.target.checked)}
          defaultChecked
        /> Road Events
      </div>
    </div>
  )
};
