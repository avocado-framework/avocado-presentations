#!/bin/bash
# (must be run as root)
mkdir /srv/tmp
echo "/tmp /srv/tmp none bind,noauto,user 0 0" >> /etc/fstab

mkdir /srv/ro
echo "/tmp /srv/ro none bind,noauto,user,ro 0 0" >> /etc/fstab
