#!/usr/bin/env bash
# A script that sets up a web server for the deployment of web_static

# update package repositories
sudo apt-get -y update

# install nginx
sudo apt-get -y install nginx

# create folders and subfolders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create fake html file for testing
echo -e "This is a test file" | sudo tee /data/web_static/releases/test/index.html

# create a new symbolic link every time the script is ran
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# give user and group ownership to ubuntu, make it recursive
sudo chown -R ubuntu:ubuntu /data/

# update nginx default config file
sudo sed -i "54i \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# restart nginx to effect changes
sudo service nginx restart

# exit program
exit 0
