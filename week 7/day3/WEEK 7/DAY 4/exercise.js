import React, { Component } from 'react';

class UserFavoriteAnimals extends Component {
  render() {
    // Destructure favAnimals from props
    const { favAnimals } = this.props;
    
    return (
      <ul>
        {favAnimals.map((animal, index) => (
          <li key={index}>{animal}</li>
        ))}
      </ul>
    );
  }
}

export default UserFavoriteAnimals;
.para {
  background-color: #282c34;
  color: white;
  padding: 40px;
  font-family: Arial;
  text-align: center;
}
import React, { Component } from 'react';
import './Exercise.css'; // Importing external CSS

class Exercise extends Component {
  render() {
    // Style object for Part II
    const style_header = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial"
    };

    return (
      <div>
        {/* Part I: Inline Styled Header */}
        <h1 style={{ color: 'red', backgroundColor: 'lightblue' }}>
          Inline Styled Header
        </h1>

        {/* Part II: Object Styled Header */}
        <h1 style={style_header}>Object Styled Header</h1>

        {/* Part III: External CSS Styled Paragraph */}
        <p className="para">This is a paragraph styled using an external CSS file.</p>

        {/* HTML Elements Section */}
        <a href="https://react.dev" target="_blank" rel="noreferrer">
          Learn React Official Link
        </a>

        <form style={{ margin: '20px 0' }}>
          <label htmlFor="username">Username: </label>
          <input type="text" id="username" placeholder="Enter name..." />
          <button type="submit">Submit</button>
        </form>

        <h3>Image Example:</h3>
        <img 
          src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=300" 
          alt="React Logo Concept" 
          style={{ borderRadius: '8px' }}
        />

        <h3>HTML List:</h3>
        <ul>
          <li>Coffee</li>
          <li>Tea</li>
          <li>Milk</li>
        </ul>
      </div>
    );
  }
}

export default Exercise;
import React from 'react';
import UserFavoriteAnimals from './UserFavoriteAnimals';
import Exercise from './Exercise3';

function App() {
  // Exercise 1 Data
  const myelement = <h1>I Love JSX!</h1>;
  const sum = 5 + 5;

  // Exercise 2 Data
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      
      {/* EXERCISE 1 */}
      <section style={{ borderBottom: '2px solid #ccc', paddingBottom: '20px' }}>
        <h2>Exercise 1: with JSX</h2>
        <p>Hello World!</p>
        {myelement}
        <p>React is {sum} times better with JSX</p>
      </section>

      {/* EXERCISE 2 */}
      <section style={{ borderBottom: '2px solid #ccc', padding: '20px 0' }}>
        <h2>Exercise 2: Object & Props</h2>
        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>
        <h4>Favorite Animals:</h4>
        <UserFavoriteAnimals favAnimals={user.favAnimals} />
      </section>

      {/* EXERCISE 3 */}
      <section style={{ paddingImg: '20px 0' }}>
        <h2>Exercise 3: HTML Tags & Styling</h2>
        <Exercise />
      </section>

    </div>
  );
}

export default App;
