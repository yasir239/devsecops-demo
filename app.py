from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    """Main endpoint that returns a welcome message."""
    return jsonify({
        "message": "Hello, DevSecOps!",
        "status": "running"
    })


@app.route("/health")
def health():
    """
    Health check endpoint used to verify that the application is running correctly.
    """
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
