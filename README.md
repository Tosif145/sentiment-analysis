# Sentiment Analysis

## Introduction
The Sentiment Analysis project consists of a Flask API for sentiment analysis and a React app for visualization. The sentiment analysis is performed on textual data, and the results are displayed using a circular progress bar.

## Project Initialization

### Prerequisites
Ensure you have the following tools installed:
- Python (for Flask)
- Node.js (for React)
- MongoDB (if using MongoDB)

### Flask API
1. **Navigate to the flask-app directory.**
2. **Install dependencies:**
   ```bash
   cd flask-app
   pip install -r requirements.txt
# Run the Flask app:
```bash
    python app.py
## React App
- Navigate to the react-app directory.
- Install dependencies:
  ```bash
      cd react-app
      npm install
## Start the React app:
```bash
    npm start
- Open the React app in your browser (usually at http://localhost:3000).
- Click the "Run Sentiment Analysis" button to trigger the sentiment analysis process.
## Circular Progress Bar
The React app includes a Circular Progress Bar component located in CircularProgressBar.js. This component fetches sentiment analysis results from the Flask API.

Customization
You can customize the circular progress bar's appearance and behavior by modifying the CSS in the CircularProgressBar.css file.

