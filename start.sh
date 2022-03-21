. venv/bin/activate
pip3 install --upgrade pip3
pip3 install -r requirements.txt
./database/create_db.sh
python3 gift-app/app.py

