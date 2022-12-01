import React, { useRef } from 'react';

import Pin from './Pin.js';

import './Routes.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLocationArrow, faPlus, faXmark } from '@fortawesome/free-solid-svg-icons';


export default function Routes({ open, routeHandler, setRoutesOpen, setStartToLocation }) {

  const inputRef = useRef(null)

  if (!open) {
    return (
      <button className="open-routes BC-Gov-PrimaryButton"
        onClick={() => setRoutesOpen(true)}
      ><FontAwesomeIcon icon={faPlus} /> Add Route</button>
    )
  }

  return (
    <div className="routes">
      <button className="close-routes"
        onClick={() => setRoutesOpen(false)}
      ><FontAwesomeIcon icon={faXmark} /></button>

      <div className="starting">
        <div className="anchor anchor-a">A</div>

        <div className="text">
          <h3>Starting Location</h3>
          <p>Drag and drop a pin or use your current location.</p>
          <div className="options">
            <div className="option">
              <div><Pin role="start" /></div>
              <div className="option-label">Drag and drop</div>
            </div>
            <div className="option" onClick={setStartToLocation}>
              <div className="current-location-icon">
                <FontAwesomeIcon icon={faLocationArrow} />
              </div>
              <div className="option-label">Use my location</div>
            </div>
          </div>
        </div>
      </div>
      <div className="starting">
        <div className="anchor anchor-b">B</div>

        <div className="text">
          <h3>Destination</h3>
          <p>Drag and drop a destination pin.</p>

          <div className="options">
            <div className="option">
              <div><Pin role="end" /></div>
              <div className="option-label">Drag and drop</div>
            </div>
          </div>
        </div>

      </div>
      <div className="notification">
        <h3>Notification Email</h3>
        <p>Notify me of any new road events along this route.</p>

        <div>
          <input className="form-route text_input" type="text" ref={inputRef} placeholder="Email address"/>
        </div>

        <button
          className='BC-Gov-PrimaryButton get-route'
          onClick={() => routeHandler(inputRef.current.value)}
        ><FontAwesomeIcon icon={faPlus} /> Add Route</button>
      </div>

    </div>
  )
};
