# nexabridge

Add the following lines to your /etc/apt/sources.list:

deb http://download.telldus.com/debian/ stable main

or

deb https://s3.eu-central-1.amazonaws.com/download.telldus.com unstable main

wget http://download.telldus.com/debian/telldus-public.key

sudo apt-key add telldus-public.key

apt update

sudo apt-get install telldus-core libtelldus-core-dev

pip install tellcore-py

sudo systemctl enable /home/pi/nexabridge/nexabridge.service

sudo service nexabridge start
