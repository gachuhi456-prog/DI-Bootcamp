import React from 'react';

// Part III: Garage Component receiving 'size' prop
function Garage(props) {
  return (
    <h3>Who lives in my {props.size} Garage?</h3>
  );
}

export default Garage;
import React, { useState } from 'react';
import Garage from './Garage';

function Car(props) {
  // Part II: useState Hook for color state
  const [color, setColor] = useState("red");

  return (
    <div>
      {/* Part I & II output */}
      <h2>This car is {color} {props.carInfo.model}</h2>
      
      {/* Part III: Rendering Garage inside Car */}
      <Garage size="small" />
    </div>
  );
}

export default Car;
import React, { useState } from 'react';

function Events() {
  // Part III: State for the toggle button
  const [isToggleOn, setIsToggleOn] = useState(true);

  // Part I: Click handler
  const clickMe = () => {
    alert('I was clicked');
  };

  // Part II: KeyDown handler
  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      alert(`The Enter key was pressed, your input is: ${event.target.value}`);
    }
  };

  // Part III: Toggle handler
  const toggleState = () => {
    setIsToggleOn(!isToggleOn);
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', margin: '10px 0' }}>
      <h3>Exercise 2: Events</h3>
      
      {/* Part I */}
      <button onClick={clickMe}>Click Me!</button>
      <br /><br />

      {/* Part II */}
      <input 
        type="text" 
        onKeyDown={handleKeyDown} 
        placeholder="Type something and press Enter..." 
      />
      <br /><br />

      {/* Part III */}
      <button onClick={toggleState}>
        {isToggleOn ? 'ON' : 'OFF'}
      </button>
    </div>
  );
}

export default Events;
import React, { useState } from 'react';

function Phone() {
  // Part I: State setup for the phone object parameters
  const [brand, setBrand] = useState("Samsung");
  const [model, setModel] = useState("Galaxy S20");
  const [color, setColor] = useState("black");
  const [year, setYear] = useState(2020);

  // Part II: Change color function
  const changeColor = () => {
    setColor("blue");
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', margin: '10px 0' }}>
      <h3>Exercise 3: Phone</h3>
      <h1>My phone is a {brand}</h1>
      <p>It is a {color} {model} from {year}</p>
      
      {/* Part II Button */}
      <button onClick={changeColor}>Change color</button>
    </div>
  );
}

export default Phone;
import React, { useState, useEffect } from 'react';

function Color() {
  const [favoriteColor, setFavoriteColor] = useState("red");

  // Part II: useEffect runs after the initial render
  useEffect(() => {
    alert("useEffect reached");
  }, []); // Empty dependency array ensures this alerts only once on mount

  // Part III: Function to update color state
  const changeToBlue = () => {
    setFavoriteColor("blue");
  };

  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', margin: '10px 0' }}>
      <h3>Exercise 4: useEffect</h3>
      <h1>My Favorite Color is <em>{favoriteColor}</em></h1>
      
      {/* Part III Button */}
      <button onClick={changeToBlue}>Change color to Blue</button>
    </div>
  );
}

export default Color;
import React from 'react';
import Car from './Components/Car';
import Events from './Components/Events';
import Phone from './Components/Phone';
import Color from './Components/Color';

function App() {
  // Exercise 1: Part I Car Info Object
  const carinfo = { name: "Ford", model: "Mustang" };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1>React Exercises XP</h1>
      <hr />
      
      {/* Exercise 1 */}
      <Car carInfo={carinfo} />
      <hr />

      {/* Exercise 2 */}
      <Events />
      <hr />

      {/* Exercise 3 */}
      <Phone />
      <hr />

      {/* Exercise 4 */}
      <Color />
    </div>
  );
}

export default App;