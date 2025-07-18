#!/bin/bash
# Local development script

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOL
DEBUG=True
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DATABASE_URL=sqlite:///./db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
EOL
fi

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser if needed
python manage.py createsuperuser --noinput --username admin --email admin@example.com || true

# Run development server
python manage.py runserver