from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route('/webhook', methods=['POST'])  # Added webhook route
def webhook():
    # Get the JSON data sent to the webhook
    data = request.json
    
    # Process the data (you can add your logic here)
    print("Received data:", data)
    
    # Respond with a success message
    return jsonify({'status': 'success', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
