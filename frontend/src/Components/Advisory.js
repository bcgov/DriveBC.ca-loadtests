import React, { useEffect, useState } from 'react';

import './Advisory.css';

export default function Advisory({ advisories }) {
  const [open, setOpen] = useState(false);

  function togglePanel(openPanel) {
    setOpen(openPanel);
  }

  if(open) {
    return (
      <div className="travel-advisory-panel-full">
        <div><button className="travel-advisory-close" onClick={() => togglePanel(false)}>X</button></div>
        <div className="travel-advisory-panel-content">
          {advisories.map((item, index) => {
            return <div key={item.id}>
              <div className="travel-advisory-header">
                Travel Advisory
                <span className="travel-advisory-header-count">{index + 1} of {advisories.length}</span>
              </div>
              <div className="travel-advisory-title">{item.title}</div>
              <div className="travel-advisory-desc">{item.text}</div>
            </div>
          })}
        </div>
      </div>
    )
  } else {
    return (
      <div className="travel-advisory-panel" onClick={() => togglePanel(true)}>
        <span className="hazard-icon"></span>Travel Advisory <span className="travel-advisory-panel-count">({advisories.length})</span>
      </div>
    )
  }

};
