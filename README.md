# jederu
This is a little panel I created for hosting a python discord bot
This is how to install it:


sudo apt-get update

curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

sudo apt-get install -y nodejs

npm install discord.js

sudo apt-get install nginx python3-pip unzip

sudo service nginx start

sudo rm /etc/nginx/sites-available/default

sudo rm /etc/nginx/sites-enabled/default

sudo nano /etc/nginx/sites-available/jederu :

server {
	location / {
		proxy_pass http://127.0.0.1:8000;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
	}
}

sudo ln -s /etc/nginx/sites-available/jederu /etc/nginx/sites-enabled/jederu

sudo service nginx restart

sudo pip3 install virtualenv

sudo mkdir jederu
sudo cd jederu/

sudo virtualenv jederu

sudo screen

sudo source jederu/bin/activate

sudo pip3 install flask pyyaml gunicorn

sudo wget https://jederu.ga/download/latest.zip

sudo unzip latest.zip

sudo gunicorn main:app



the default username: admin
the default password: test123
you can edit the usernames and/or passwords or create new accounts in data/accounts.yml

Note: you can't use more than 1 account with the same name!!
