# build_files.sh
pip install --upgrade pip
pip install -r requirements.txt
pip install apturl

# make migrations
python3 manage.py migrate 
python3 manage.py collectstatic