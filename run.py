# app.py
from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the health check endpoint
print("welcome server ")
@app.route('/health', methods=['GET'])

def health_check():
    return jsonify({"status": "ok"}), 200
@app.route('/hlt', methods=['GET'])
def health1_check():
    return jsonify({"status": "new route "}), 200
@app.route('/', methods=['GET'])
def health2_check():
    return jsonify({"status": "Welcome to Flask server"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
