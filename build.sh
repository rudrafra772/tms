#!/usr/bin/env bash
# Exit on error
set -o errexit

ls

cat .env

echo "Updating package list and installing required packages..."
apt-get update && apt-get install -y 
echo "Package installation complete."

echo "Creating virtual environment..."
python -m venv env
echo "Virtual environment created."

echo "Activating virtual environment..."
source env/bin/activate
echo "Virtual environment activated."

echo "Upgrading pip..."
python3 -m pip install --upgrade pip
echo "Pip upgrade complete."


# Step 5: Install 'wheel' package
echo "Installing 'wheel' package..."
pip install --no-cache-dir wheel
echo "'Wheel' package installation complete."


# Modify this line as needed for your package manager (pip, poetry, etc.)
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
echo "Dependencies installation complete."

# Convert static asset files
echo "Collecting static files..."
python manage.py collectstatic --no-input
echo "Static files collection complete."

# Apply any outstanding database migrations
echo "Applying database migrations..."
python manage.py migrate
echo "Database migrations complete."

echo "Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:8000 tms.wsgi
echo "Gunicorn server started."

# if [[ $CREATE_SUPERUSER ]];
# then
#   python world_champ_2022/manage.py createsuperuser --no-input
# fi