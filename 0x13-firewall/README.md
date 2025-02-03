## 0x13-firewall
This directory contains a project task to configure a web server's firewall
to deny all incoming traffic except from ports 80, 22 and 443

sudo ufw disable
sudo ufw default deny incoming
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
