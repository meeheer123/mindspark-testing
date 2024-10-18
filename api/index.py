import os
from flask import Flask, jsonify
from datadog import initialize, api

app = Flask(__name__)

# Initialize Datadog with your API key
options = {
    'api_key': os.getenv('DATADOG_API_KEY'),  # Make sure this is set in Vercel environment variables
}

initialize(**options)

# Function to log error to Datadog
def log_error_to_datadog(error_message):
    api.Event.create(
        title="Application Error",
        text=error_message,
        alert_type="error"
    )

# Example route that may cause an error
@app.route('/')
def home():
    try:
        result = 1 / 0  # Intentional error
        return jsonify({"result": result})
    except Exception as e:
        # Log the error to Datadog
        log_error_to_datadog(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500

# Run the app (you may not need this depending on how Vercel handles your app)
if __name__ == '__main__':
    app.run(debug=True)
