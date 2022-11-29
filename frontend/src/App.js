import React from 'react'
import { DndProvider } from 'react-dnd'
import { HTML5Backend } from 'react-dnd-html5-backend'

import './App.css';

import Map from './Components/Map.js';

function App() {
  return (
    <DndProvider backend={HTML5Backend}>
      <div className="App">
        <header>Drive BC</header>
        <Map />
      </div>
        
    </DndProvider>
  );
}

export default App;
