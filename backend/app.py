from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the API", "status": "running"})


@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "service": "backend"})


@app.route("/api/data")
def get_data():
    return jsonify(
        {
            "items": [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"},
                {"id": 3, "name": "Item 3"},
            ]
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
