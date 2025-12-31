# Growthify Backend

This is the Django backend for Growthify Services.

## Prerequisites

- Python 3.8+ (for manual setup)
- Docker and Docker Compose (optional, for containerized setup)

## Manual Setup

1.  **Create and activate virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create superuser (optional):**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Start the server:**
    ```bash
    python manage.py runserver
    ```

    Api running at: `http://localhost:8000`

## Docker Setup

The backend is configured with `docker-compose.yml` which includes a PostgreSQL database.

1.  **Start the services:**
    ```bash
    docker-compose up --build
    ```

    This will start the Django backend on port 8000 and the PostgreSQL database.

    Access the API at `http://localhost:8000/api`.
    Access the Admin Setup at `http://localhost:8000/admin`.
