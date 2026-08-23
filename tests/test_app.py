import pytest
from app import app


# ─── Fixture ────────────────────────────────────────────────────────────────
@pytest.fixture
def client():
    """
    ينشئ test client مؤقت للتطبيق.
    TESTING=True يعني Flask لن يخفي الأخطاء — مفيد عند الاختبار.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ─── Tests ──────────────────────────────────────────────────────────────────
def test_hello_endpoint(client):
    """
    اختبار الـ endpoint الرئيسي GET /
    نتحقق من:
    1. الـ status code = 200 (نجح الطلب)
    2. الـ response يحتوي على "Hello, DevSecOps!"
    """
    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, DevSecOps!"
    assert data["status"] == "running"


def test_health_endpoint(client):
    """
    اختبار الـ health check endpoint GET /health
    نتحقق من:
    1. الـ status code = 200
    2. الـ status = "healthy"
    """
    response = client.get("/health")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_unknown_route_returns_404(client):
    """
    اختبار أن route غير موجود يرجع 404.
    هذا يتحقق أن Flask يتعامل مع الـ routes بشكل صحيح.
    """
    response = client.get("/does-not-exist")

    assert response.status_code == 404
