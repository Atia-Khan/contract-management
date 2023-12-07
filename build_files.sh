# build_files.sh
# pip install --upgrade pip
source env/bin/activate
pip install -r requirements.txt

# make migrations
python3 manage.py migrate 
python3 manage.py collectstatic