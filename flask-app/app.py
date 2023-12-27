# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
from analysis_model import perform_analysis
import subprocess
import numpy as np

app = Flask(__name__)
CORS(app)

# Function to run the analysis and predictor scripts
def run_analysis_and_predictor():
    try:
        # Run the analysis script
        subprocess.run(['python', 'analysis_model.py'], check=True)

        # Run the predictor script
        subprocess.run(['python', 'predictor.py'], check=True)

        # Load the predicted labels and sentiment result after running the predictor script
        predicted_labels = np.loadtxt('predicted_labels.txt', dtype=int)
        sentiment_result = calculate_sentiment_result(predicted_labels)

        return predicted_labels, sentiment_result

    except Exception as e:
        print(f"Error during analysis and prediction: {e}")
        return None, None

# Function to calculate sentiment result
def calculate_sentiment_result(predicted_labels):
    positive_count = np.sum(predicted_labels == 1)
    total_count = len(predicted_labels)
    sentiment_result = (positive_count / total_count) * 100 if total_count > 0 else 0
    return sentiment_result

# Trigger the analysis and predictor on startup
predicted_labels, initial_sentiment_result = run_analysis_and_predictor()

# Handle the API request
@app.route('/api/sentiment', methods=['GET', 'POST'])
def sentiment_analysis():
    global predicted_labels

    if request.method == 'GET':
        try:
            # Compute sentiment_result based on the frequency of positive labels
            sentiment_result = calculate_sentiment_result(predicted_labels)

            # Print sentiment_result to the console
            print("Sentiment Result:", sentiment_result)

            # Return sentiment result and predicted labels in the JSON response
            response_data = {'sentiment': sentiment_result, 'predicted_labels': predicted_labels.tolist()}

            return jsonify(response_data)

        except Exception as e:
            print("Error during sentiment analysis:", e)
            return jsonify({'error': 'Internal Server Error'}), 500
        

    
@app.route('/start-apps', methods=['GET'])
def start_apps():
    try:
        # Start both apps using the script
        subprocess.run(['python', 'run_apps.py'], check=True)
        return jsonify({'message': 'Apps started successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
