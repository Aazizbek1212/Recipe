#!/bin/bash

# Activate your virtual environment
source venv/bin/activate

# Pull the latest changes
git pull origin main

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic --noinput

sudo systemctl restart Recipe