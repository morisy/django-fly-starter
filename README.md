# Django Fly.io Starter

Get a Django app running locally and deployed to Fly.io in under 5 minutes.

## Quick Start

### 1. Use this template and clone
```bash
# Clone and rename
git clone https://github.com/morisy/django-fly-starter.git new-app-name
cd new-app-name

# Remove git history and start fresh
rm -rf .git
git init
```

### 2. Run locally (2 minutes)
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install and configure
pip install -r requirements.txt
cp .env.example .env  # or create .env with: echo "DEBUG=True\nSECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')\nDATABASE_URL=sqlite:///./db.sqlite3\nALLOWED_HOSTS=localhost,127.0.0.1" > .env

# Run
python manage.py migrate
python manage.py runserver
```

Visit http://localhost:8000 - you should see "Hello, Fly!"

### 3. Deploy to Fly.io (3 minutes)
```bash
# Install Fly CLI if needed: https://fly.io/docs/hands-on/install-flyctl/
fly auth login

# Launch app
fly launch --name your-app-name

# Set production secret
fly secrets set SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"

# Deploy
fly deploy

# Open in browser
fly open
```

## What You Get

- Django app configured for production
- SQLite database (upgrade to PostgreSQL later if needed)
- Static files served with WhiteNoise
- Health check endpoint at `/health/`

## Next Steps

- Create a superuser: `python manage.py createsuperuser`
- Access admin at `/admin/`
- Start building your app in a new Django app: `python manage.py startapp myapp`

---

## Additional Details

### Prerequisites

- Python 3.11+
- Git
- Fly CLI ([install instructions](https://fly.io/docs/hands-on/install-flyctl/))

### Project Structure

- `fly_starter/` - Django project directory
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration for Fly.io
- `fly.toml` - Fly.io deployment configuration
- `.env` - Local environment variables (not committed to git)
- `run_local.sh` - Convenience script for local development

### Configuration Notes

- Uses SQLite database by default (data will be lost on redeploys)
- WhiteNoise configured for static file serving
- Security settings enabled for production (HTTPS redirect, secure cookies, etc.)
- CORS headers middleware included

### Environment Variables

- `SECRET_KEY` - Django secret key (required)
- `DEBUG` - Debug mode (default: False)
- `DATABASE_URL` - Database connection string (default: SQLite)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts

### Common Commands

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

### Troubleshooting

If you encounter issues:

1. Check logs: `fly logs`
2. Ensure all environment variables are set: `fly secrets list`
3. Verify the app is running: `fly status`
4. SSH into the container for debugging: `fly ssh console`
