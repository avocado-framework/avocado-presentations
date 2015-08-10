#!/bin/bash -e

# Make sure the mount point is not mounted previously
grep -q -v /srv/tmp /proc/mounts || umount /srv/tmp

mount /srv/tmp
grep -q /srv/tmp /proc/mounts && echo 'PASS: Mount test' || echo 'FAIL: Mount test'

umount /srv/tmp
grep -q -v /srv/tmp /proc/mounts && echo 'PASS: Umount test' || echo 'FAIL: Umount test'
