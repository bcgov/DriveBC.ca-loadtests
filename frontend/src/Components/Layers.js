import React, { useRef, useEffect, useState } from 'react';

import './Layers.css';


export default function Layers(props) {

  // const [open, setOpen] = useState(false);

  if (!props.open) {
    return (
      <button className="open-layers"
        onClick={() => props.setLayersOpen(true)}
      >L</button>
    )
  }

  return (
    <div className="layers">
      <button className="close-layers"
        onClick={() => props.setLayersOpen(false)}
      >X</button>
      <h3>Base Layers</h3>
      <div className="layers-select">
        <div className="panel">
          <div className="icon"></div>
          <div>Map</div>
        </div>
        <div className="panel">
          <div className="icon"></div>
          <div>Terrain</div>
        </div>
      </div>
      <h3>Features</h3>
      <div>
        <input type="checkbox" /> Webcam
      </div>
      <div>
        <input type="checkbox" /> Road Events
      </div>
    </div>
  )
};
