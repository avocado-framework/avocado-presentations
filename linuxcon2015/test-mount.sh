#!/bin/bash -e

mount /srv/tmp
grep -q /srv/tmp /proc/mounts

umount /srv/tmp
grep -qv /srv/tmp /proc/mounts

echo 'PASS: Mount/Unmount Test'
