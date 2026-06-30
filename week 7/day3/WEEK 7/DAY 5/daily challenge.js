import React, { useState } from 'react';
import './App.css'; // Optional: for your styling

function App() {
  // 1. Initialize state with the array of language objects
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaScript", votes: 0 }, // Fixed a tiny typo in JavaScript!
    { name: "Java", votes: 0 }
  ]);

  // 2. Function to increase votes by one for a specific language
  const handleVote = (index) => {
    // We map over the existing array to create a brand new one
    const updatedLanguages = languages.map((lang, i) => {
      if (i === index) {
        // Return a new object with the incremented vote count
        return { ...lang, votes: lang.votes + 1 };
      }
      // Leave all other languages exactly as they were
      return lang;
    });

    // Update the state with our new array
    setLanguages(updatedLanguages);
  };

  return (
    <div className="voting-container" style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h2>Vote Your Favorite Language</h2>
      
      <div className="languages-list" style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '300px' }}>
        {languages.map((lang, index) => (
          <div 
            key={lang.name} 
            className="language-card" 
            style={{ 
              display: 'flex', 
              justifyContent: 'space-between', 
              alignItems: 'center', 
              padding: '10px', 
              border: '1px solid #ccc',
              borderRadius: '5px'
            }}
          >
            {/* Displaying total votes */}
            <span className="vote-count" style={{ fontWeight: 'bold', marginRight: '10px' }}>
              {lang.votes}
            </span>

            {/* Displaying language name */}
            <span className="language-name" style={{ flexGrow: 1 }}>
              {lang.name}
            </span>

            {/* Button to trigger the vote function */}
            <button 
              onClick={() => handleVote(index)}
              style={{ padding: '5px 10px', cursor: 'pointer' }}
            >
              Click Here
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;