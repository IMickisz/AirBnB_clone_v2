# Task #0 (sets up your web servers for the deployment of web_static) but by using Puppet

exec { '/usr/bin/env apt-get -y update': }
-> exec { '/usr/bin/env apt-get -y install nginx': }
-> exec { '/usr/bin/env mkdir -p /data/web_static/releases/test/': }
-> exec { '/usr/bin/env mkdir -p /data/web_static/shared/': }
-> exec { '/usr/bin/env echo "Hello Holberton !" > /data/web_static/releases/test/index.html': }
-> exec { '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current': }
-> exec { '/usr/bin/env chown -R ubuntu:ubuntu /data/': }
-> exec { '/usr/bin/env sed -i "47i location /hbnb_static { alias /data/web_static/current/; }" /etc/nginx/sites-available/default': }
-> exec { '/usr/bin/env service nginx restart': }
