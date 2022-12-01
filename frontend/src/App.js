import React from 'react'
import { DndProvider } from 'react-dnd'
import { HTML5Backend } from 'react-dnd-html5-backend'

import './App.css';
import Logo from './Components/Logo.js';
import Map from './Components/Map.js';

import '@bcgov/bc-sans/css/BCSans.css';

function App() {
  return (
    <DndProvider backend={HTML5Backend}>
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
