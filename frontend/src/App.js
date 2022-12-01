import React from 'react'
import { DndProvider } from 'react-dnd-multi-backend'
import { HTML5toTouch } from 'rdndmb-html5-to-touch'

import './App.css';
import Logo from './Components/Logo.js';
import Map from './Components/Map.js';

import '@bcgov/bc-sans/css/BCSans.css';

function App() {
  return (
    <DndProvider options={HTML5toTouch}>
      <div className="App">
        <header>
          <div className="banner">
            <a href="https://gov.bc.ca">
            <Logo className="logo" />
            </a>
          </div>
          <div className="other">
            <h2>DriveBC</h2>
          </div>
        </header>

        <Map />
      </div>
    </DndProvider>
  );
}

export default App;
