# build_files.sh
# pip install --upgrade pip
# pip install virtualenv
# pip virtualenv venv
# apt-get install gettext

# source venv/bin/activate
# pip install -r requirements.txt

# # make migrations
# python3 manage.py migrate 
# python3 manage.py collectstatic


#!/bin/bash
# Install or upgrade pip
# pip install --upgrade pip
# Install virtualenv
pip install virtualenv
# Create a virtual environment
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install gettext (needed for msgfmt command)
# Ensure that the system packages are up-to-date
apt-get update
# Install gettext
apt-get install -y gettext
# Install Python dependencies
pip install --disable-pip-version-check --upgrade -r requirements.txt
# Make sure the environment variables are set
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
# Make migrations
python manage.py migrate
# Collect static files
python manage.py collectstatic