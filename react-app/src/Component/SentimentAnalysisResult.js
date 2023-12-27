import React from 'react';
import CircularProgressBar from './CircularProgressBar';

const SentimentAnalysisResult = ({ result }) => {
  return (
    <div>
      <h2>Sentiment Analysis Result:</h2>
      <CircularProgressBar percentage={result} />
    </div>
  );
};

export default SentimentAnalysisResult;
