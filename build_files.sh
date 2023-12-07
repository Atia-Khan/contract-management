# build_files.sh
pip install --upgrade pip
pip install apturl==0.4
pip install -r requirements.txt

# make migrations
python3 manage.py migrate 
python3 manage.py collectstatic