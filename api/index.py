import sentry_sdk
import requests
from flask import Flask

# Define your API endpoint
MY_API_ENDPOINT = "https://2874-210-212-183-2.ngrok-free.app/error-handler"

# Sentry initialization
sentry_sdk.init(
    dsn="https://72abbb6de5212124591b8e322042c19a@o4508146106630144.ingest.us.sentry.io/4508146141102080",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    before_send=lambda event, hint: send_error_to_api(event)  # Intercept the error before sending to Sentry
) 

@app.route("/error-handler", methods=["POST"])
def error_handler():
    # Get the error data sent by Sentry
    error_data = request.get_json()

    if not error_data:
        return jsonify({"message": "No error data received"}), 400

    # Extract the error type and description from the error data
    try:
        error_type = error_data['exception']['values'][0]['type']
        error_description = error_data['exception']['values'][0]['value']
    except (KeyError, IndexError) as e:
        error_type = "Unknown Error"
        error_description = "Error extracting error details"

    # Print or log the error type and description
    print(f"Error Type: {error_type}")
    print(f"Description: {error_description}")

    # Optionally, log the entire error data to a file or database
    log_to_file_or_db(error_data)

    # Respond with a success message
    return jsonify({
        "message": "Error received and processed",
        "error_type": error_type,
        "description": error_description
    }), 200


# Flask app
app = Flask(__name__)

@app.route("/")
def hello_world():  # Raises an error
    1/0
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
