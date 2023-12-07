# build_files.sh
# pip install --upgrade pip
pip install virtualenv
pip virtualenv venv
apt-get install gettext

source venv/bin/activate
pip install -r requirements.txt

# make migrations
python3 manage.py migrate 
python3 manage.py collectstatic