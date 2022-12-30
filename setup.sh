pkg update
pkg install python -y
pkg install openssl -y
pkg install wget -y
pip install pyTelegramBotAPI



wget https://raw.githubusercontent.com/Mihalic2040/SvitloBot/main/main.py


touch DB.txt

clear

echo "INPUT TELEGRAM TOKEN: "

read token

not_token='"'$token'"'

echo "bottoken = "$not_token > seting.py

echo "ALL OK"

wget https://raw.githubusercontent.com/Mihalic2040/SvitloBot/main/s.sh

chmod +x s.sh