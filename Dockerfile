FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

# ✅ Ye line change karo
CMD python manage.py migrate && \
    python manage.py load_initial_data.json && \
    gunicorn growthify.wsgi:application --bind 0.0.0.0:8000
