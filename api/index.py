import sentry_sdk
import requests
from flask import Flask

# Define your API endpoint
MY_API_ENDPOINT = "https://foremost-sweltering-dew.glitch.me/error-handler"

# Sentry initialization
sentry_sdk.init(
    dsn="https://799617a61eb573bcc80f41a17fb07a30@o4508148663910400.ingest.us.sentry.io/4508148665155584",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    before_send=lambda event, hint: send_error_to_api(event)  # Intercept the error before sending to Sentry
) 

# Function to send error details to your API
def send_error_to_api(event):
    try:
        # Send event to your custom API
        response = requests.post(MY_API_ENDPOINT, json=event)
        print(f"Response from API: {response.status_code} - {response.text}")
        response.raise_for_status()  # Raise an exception for non-200 responses
    except requests.exceptions.RequestException as e:
        print(f"Failed to send error to API: {e}")
    return event  # Return event to proceed with Sentry reporting

# Flask app
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(helloworlx
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
