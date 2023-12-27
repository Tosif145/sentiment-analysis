// CircularProgressBar.js

import React, { useState } from 'react';
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import axios from 'axios';
import '../css/index.css'; // Import the CSS file

const CircularProgressBar = () => {
  const [sentimentScore, setSentimentScore] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [paragraphContent, setParagraphContent] = useState('');
  const [leftStr,setLeft] = useState('');
  const [rightStr,setRight] = useState(' ');
  const handleRunButtonClick = async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await axios.get('http://localhost:5000/api/sentiment');
      const sentiment = response.data.sentiment;
      setSentimentScore(sentiment);
      setLeft('we have received');
      setRight('positve reviews !');
      setParagraphContent(` ${sentiment}% `);
    } catch (error) {
      console.error('Error fetching sentiment score:', error);
      setError('Error fetching sentiment score. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="circular-progress-container">
      <div className="circular-progress-bar">
        <CircularProgressbar value={sentimentScore !== null ? sentimentScore : 0} text={`${sentimentScore || 0}%`} />
      </div>
      <p className='content'>{leftStr}<span>{paragraphContent}</span>{rightStr}</p>
      <button className="run-button" onClick={handleRunButtonClick} disabled={loading}>
        {loading ? 'Running...' : 'Run Sentiment Analysis'}
      </button>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default CircularProgressBar;
