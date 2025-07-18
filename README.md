# Django Fly.io Starter

A Django starter template configured for deployment on Fly.io. These instructions were designed for Mac OS X but should work with minor modifications elsewhere.

## Prerequisites

- Python 3.11+
- Fly CLI ([install instructions](https://fly.io/docs/hands-on/install-flyctl/))

## Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd fly-starter
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file for local development:
```bash
cat > .env << EOF
DEBUG=True
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DATABASE_URL=sqlite:///./db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
EOF
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The app will be available at http://localhost:8000

## Deploying to Fly.io

1. Authenticate with Fly:
```bash
fly auth login
```

2. Launch the app (first time only):
```bash
fly launch --name your-app-name
```
- Choose your preferred region
- Select "No" when asked about PostgreSQL database (unless you want to use PostgreSQL)
- Select "No" when asked about Redis

3. Set production environment variables:
```bash
fly secrets set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
```

4. Deploy:
```bash
fly deploy
```

5. Open your app:
```bash
fly open
```

## Project Structure

- `fly_starter/` - Django project directory
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration for Fly.io
- `fly.toml` - Fly.io deployment configuration
- `.env` - Local environment variables (not committed to git)
- `run_local.sh` - Convenience script for local development

## Configuration Notes

- Uses SQLite database by default (data will be lost on redeploys)
- WhiteNoise configured for static file serving
- Security settings enabled for production (HTTPS redirect, secure cookies, etc.)
- CORS headers middleware included

## Environment Variables

- `SECRET_KEY` - Django secret key (required)
- `DEBUG` - Debug mode (default: False)
- `DATABASE_URL` - Database connection string (default: SQLite)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts

## Common Commands

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# View Fly.io logs
fly logs

# SSH into running container
fly ssh console

# Scale app
fly scale count 2
```

## Troubleshooting

If you encounter issues:

1. Check logs: `fly logs`
2. Ensure all environment variables are set: `fly secrets list`
3. Verify the app is running: `fly status`
4. SSH into the container for debugging: `fly ssh console`