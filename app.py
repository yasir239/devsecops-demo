from flask import Flask, jsonify

# إنشاء instance من Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """Endpoint رئيسي - يرجع رسالة ترحيب."""
    return jsonify({
        "message": "Hello, DevSecOps!",
        "status": "running"
    })


@app.route("/health")
def health():
    """
    Health check endpoint.
    يُستخدم في DevOps للتحقق أن التطبيق يعمل بشكل صحيح.
    """
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    # host="0.0.0.0" مهم داخل Docker ليستقبل الطلبات من خارج الـ container
    app.run(host="0.0.0.0", port=5000, debug=False)
