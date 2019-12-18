import React from 'react';
import './App.css';
import Navigation from './components/Navigation';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Navigation/>
      </header>
    </div>
  );
}

export default App;
