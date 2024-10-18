from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # This will cause an error, as 'undefined_variable' is not defined
    return jsonify(message="Hello World!", value=undefined_variable)

if __name__ == '__main__':
    app.run(debug=True)
