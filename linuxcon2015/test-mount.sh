#!/bin/bash -e

mount /srv/tmp
grep -p /srv/tmp /proc/mounts

umount /srv/tmp
grep -pv /srv/tmp /proc/mounts
