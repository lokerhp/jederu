# jederu
This is a little panel I created for hosting a python discord bot
This is how to install it:
sudo apt-get update

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

pip3 install virtualenv

mkdir jederu
cd jederu/

virtualenv jederu

screen

source jederu/bin/activate

pip3 install flask pyyaml gunicorn

wget https://jederu.ga/download/latest.zip

unzip latest.zip

gunicorn main:app
