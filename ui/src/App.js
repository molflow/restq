import React from 'react';
import restq from './restq.svg';
import './App.css';
import Usage from './Usage.js';

const App = () => (
  <div className="App">
    <div className="App-header">
      <img src={restq} className="App-logo" alt="logo" />
      <h2>Welcome to restq</h2>
    </div>
    <Usage />
  </div>
);

export default App;
