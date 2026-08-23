# DevSecOps Demo — مشروع تعليمي

مشروع Web API بسيط يُطبّق **CI/CD pipeline** كامل باستخدام GitHub Actions.

## 🏗️ هيكل المشروع

```
devsecops-demo/
├── app.py                          ← Flask application
├── requirements.txt                ← Python dependencies
├── Dockerfile                      ← Docker build instructions
├── sonar-project.properties        ← SonarCloud configuration
├── tests/
│   ├── __init__.py
│   └── test_app.py                 ← Pytest tests
└── .github/
    └── workflows/
        └── ci.yml                  ← GitHub Actions pipeline
```

## 🔄 CI/CD Pipeline

```
Git Push
    ↓
GitHub Actions
    ↓
1. 🧪 Run Tests (pytest + coverage)
    ↓
2. 🔍 SonarCloud SAST Analysis
    ↓
3. 🐳 Docker Build
    ↓
4. 🛡️ Trivy Image Scan
    ↓
5. 📦 Push to GHCR
    ↓
6. 🚀 Deploy
```

## 🚀 تشغيل محلياً

```bash
# تثبيت المكتبات
pip install -r requirements.txt

# تشغيل التطبيق
python app.py

# تشغيل الـ Tests
pytest tests/ -v
```

## 🐳 تشغيل عبر Docker

```bash
# بناء الصورة
docker build -t devsecops-demo .

# تشغيل الـ container
docker run -p 5000:5000 devsecops-demo
```

## 📡 Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | `/`       | Hello message            |
| GET    | `/health` | Health check (200 OK)    |

## 🔐 Secrets المطلوبة في GitHub

| Secret       | المصدر                        | الاستخدام           |
|--------------|-------------------------------|---------------------|
| `SONAR_TOKEN`| SonarCloud → My Account → Security | تحليل الكود بـ SonarCloud |
| `GITHUB_TOKEN` | تلقائي من GitHub           | GHCR push & SonarCloud |
