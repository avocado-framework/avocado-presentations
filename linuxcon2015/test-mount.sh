#!/bin/bash

FAIL=0
MOUNT_POINT="/srv/tmp"
PROC_MOUNTS="/proc/mounts"

check() {
    $1
    if [ $? != 0 ]; then
        FAIL=1
        echo "FAIL: $2"
    else
        echo "PASS: $2"
    fi
}

mount_test() {
    mount $1
    check "grep -q $1 /proc/mounts" 'Mount Test'
}

umount_test() {
    umount $1
    check "grep -q -v $1 /proc/mounts" 'Umount Test'
}

# Make sure the mount point is not mounted previously
grep -q -v $MOUNT_POINT $PROC_MOUNTS || umount $MOUNT_POINT
mount_test $MOUNT_POINT
umount_test $MOUNT_POINT

# Report failures
exit $FAIL
