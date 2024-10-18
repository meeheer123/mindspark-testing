from flask import Flask, jsonify
import requests
import traceback

app = Flask(__name__)

def send_error_to_api(error_details):
    api_url = "https://your-error-reporting-api.com/errors"
    try:
        response = requests.post(api_url, json=error_details)
        response.raise_for_status()
        print("Error sent to API successfully")
    except requests.RequestException as e:
        print(f"Failed to send error to API: {e}")

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/error')
def trigger_error():
    try:
        # Intentionally raise an error
        raise ValueError("This is a test error")
    except Exception as e:
        error_details = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "traceback": traceback.format_exc()
        }
        send_error_to_api(error_details)
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)