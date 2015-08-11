#!/bin/bash -e

# Installs/Configures Apache to serve user content
# Must be run as root

dnf -y install httpd
setsebool -P httpd_enable_homedirs=on
sed -e 's/UserDir\ disabled/UserDir\ enabled/' -i /etc/httpd/conf.d/userdir.conf
sed -e 's/#UserDir\ public_html/UserDir\ public_html/' -i /etc/httpd/conf.d/userdir.conf
systemctl start httpd.service
systemctl enable httpd.service
systemctl status httpd.service
