from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])  # Ensure the method is POST
def webhook():
    data = request.json  # Get the incoming JSON data
    print("Received webhook data:", data)  # Log the received data
    return jsonify({"status": "success", "data": data}), 200  # Send a success response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the app
