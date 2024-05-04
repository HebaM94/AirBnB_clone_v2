#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static


sudo apt-get update
sudo apt-get -y install nginx


sudo mkdir -p /data/web_static/releases/test /data/web_static/shared


echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'| sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


sudo chown -R ubuntu:ubuntu /data/


config_file="/etc/nginx/sites-available/default"
sudo sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' $config_file

sudo service nginx restart
