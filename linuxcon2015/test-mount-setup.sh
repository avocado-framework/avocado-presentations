#!/bin/bash
# (must be run as root)
mkdir -p /srv/tmp
grep -q '/tmp /srv/tmp none bind,noauto,user 0 0' /etc/fstab || echo '/tmp /srv/tmp none bind,noauto,user 0 0' >> /etc/fstab
