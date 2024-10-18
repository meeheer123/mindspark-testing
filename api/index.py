from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])  # Ensure the method is GET
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the app
 