# ── Stage 1: Base Image ──────────────────────────────────────────────────────
# python:3.11-slim = Python + Linux أساسي فقط بدون أدوات زيادة
# slim تعني الصورة صغيرة الحجم → أسرع في الـ pull وأقل ثغرات أمنية
FROM python:3.11-slim

# ── Stage 2: Working Directory ───────────────────────────────────────────────
# كل الأوامر التالية ستُنفَّذ داخل /app داخل الـ container
WORKDIR /app

# ── Stage 3: Install Dependencies ────────────────────────────────────────────
# ننسخ requirements أولاً قبل بقية الكود — لماذا؟
# Docker يحفظ كل COPY+RUN في "layer" مؤقتة.
# إذا لم يتغير requirements.txt، Docker يستخدم الـ cache ولا يعيد التثبيت.
# هذا يوفر وقتاً كبيراً عند البناء المتكرر.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir = لا تحفظ cache للـ pip داخل الصورة → حجم أصغر

# ── Stage 4: Copy Application Code ───────────────────────────────────────────
COPY . .

# ── Stage 5: Expose Port ──────────────────────────────────────────────────────
# توثيق فقط — لا "يفتح" المنفذ فعلاً، لكنه يخبر من يقرأ الـ Dockerfile
# أن التطبيق يعمل على port 5000
EXPOSE 5000

# ── Stage 6: Run Application ─────────────────────────────────────────────────
# الأمر الذي يُشغَّل عند بدء الـ container
CMD ["python", "app.py"]
