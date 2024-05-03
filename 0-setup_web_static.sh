#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static


sudo apt-get update
sudo apt-get -y install nginx


sudo mkdir -p /data/web_static/releases/test /data/web_static/shared


echo "<html><head></head><body>Test HTML file</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


sudo chown -R ubuntu:ubuntu /data/


config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^\s*location \/hbnb_static/{
  N
  N
  s/\(.*\)\n\( *\)\(location \/hbnb_static\)/\1\n\2alias \/data\/web_static\/current\/;\n\2\3/
}' "$config_file"

sudo service nginx restart
