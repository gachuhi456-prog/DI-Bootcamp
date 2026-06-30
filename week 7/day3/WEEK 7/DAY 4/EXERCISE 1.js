import React, { Component } from 'react';

class UserFavoriteAnimals extends Component {
  render() {
    // Destructure favAnimals from props
    const { favAnimals } = this.props;

    return (
      <div>
        <h4>Favorite Animals:</h4>
        <ul>
          {favAnimals.map((animal, index) => (
            <li key={index}>{animal}</li>
          ))}
        </ul>
      </div>
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
}import React, { Component } from 'react';
import './Exercise.css'; // Import the CSS file for Part III

class Exercise extends Component {
  render() {
    // Styling object for Part II
    const style_header = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial"
    };

    return (
      <div style={{ border: '1px solid #ccc', padding: '20px', marginTop: '20px' }}>
        {/* H1 using style_header from Part II */}
        <h1 style={style_header}>This is a Heading</h1>
        
        {/* Paragraph using the CSS class from Part III */}
        <p className="para">This is a styled paragraph from Exercise 3.</p>
        
        {/* Link */}
        <a href="https://react.dev" target="_blank" rel="noreferrer">
          Click here to visit React Official Docs
        </a>
        
        {/* Form */}
        <form style={{ margin: '20px 0' }}>
          <h3>Input Form</h3>
          <input type="text" placeholder="Enter something..." />
          <button type="submit">Submit</button>
        </form>
        
        {/* Image */}
        <h3>An Image</h3>
        <img 
          src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=300" 
          alt="React logo placeholder" 
        />
        
        {/* List */}
        <h3>An Ordered List</h3>
        <ol>
          <li>First HTML Tag element</li>
          <li>Second HTML Tag element</li>
          <li>Third HTML Tag element</li>
        </ol>
      </div>
    );
  }
}

export default Exercise;
import React, { Component } from 'react';
import './Exercise.css'; // Import the CSS file for Part III

class Exercise extends Component {
  render() {
    // Styling object for Part II
    const style_header = {
      color: "white",
      backgroundColor: "DodgerBlue",
      padding: "10px",
      fontFamily: "Arial"
    };

    return (
      <div style={{ border: '1px solid #ccc', padding: '20px', marginTop: '20px' }}>
        {/* H1 using style_header from Part II */}
        <h1 style={style_header}>This is a Heading</h1>
        
        {/* Paragraph using the CSS class from Part III */}
        <p className="para">This is a styled paragraph from Exercise 3.</p>
        
        {/* Link */}
        <a href="https://react.dev" target="_blank" rel="noreferrer">
          Click here to visit React Official Docs
        </a>
        
        {/* Form */}
        <form style={{ margin: '20px 0' }}>
          <h3>Input Form</h3>
          <input type="text" placeholder="Enter something..." />
          <button type="submit">Submit</button>
        </form>
        
        {/* Image */}
        <h3>An Image</h3>
        <img 
          src="https://images.unsplash.com/photo-1633356122544-f134324a6cee?w=300" 
          alt="React logo placeholder" 
        />
        
        {/* List */}
        <h3>An Ordered List</h3>
        <ol>
          <li>First HTML Tag element</li>
          <li>Second HTML Tag element</li>
          <li>Third HTML Tag element</li>
        </ol>
      </div>
    );
  }
}

export default Exercise;
import React from 'react';
import './App.css';
import UserFavoriteAnimals from './UserFavoriteAnimals';
import Exercise from './Exercise3';

function App() {
  // Exercise 1 elements
  const myelement = <h1>I Love JSX!</h1>;
  const sum = 5 + 5;

  // Exercise 2 object
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
  };

  return (
    <div className="App" style={{ padding: '30px', textAlign: 'left' }}>
      
      {/* --- EXERCISE 1 --- */}
      <section style={{ marginBottom: '40px' }}>
        <h2>Exercise 1: with JSX</h2>
        <p>Hello World!</p>
        {myelement}
        <p>React is {sum} times better with JSX</p>
      </section>

      <hr />

      {/* --- EXERCISE 2 --- */}
      <section style={{ margin: '40px 0' }}>
        <h2>Exercise 2: Object</h2>
        <h3>{user.firstName}</h3>
        <h3>{user.lastName}</h3>
        {/* Passing the array down via props */}
        <UserFavoriteAnimals favAnimals={user.favAnimals} />
      </section>

      <hr />

      {/* --- EXERCISE 3 --- */}
      <section style={{ marginTop: '40px' }}>
        <h2>Exercise 3: HTML Tags in React</h2>
        <Exercise />
      </section>

    </div>
  );
}

export default App;
