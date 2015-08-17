#!/bin/bash -e

SOURCE_DIR=~/src/qemu
GIT_BRANCH=master
#GIT_PULL=1
TARGETS="x86_64 i386 arm"

if [ -n "$GIT_PULL" ]; then
    cd $SOURCE_DIR
    git pull
fi

for t in $TARGETS; do
    echo "Building $t"
    BUILD_DIR="$SOURCE_DIR/build/$t"
    mkdir -p $BUILD_DIR
    cd $BUILD_DIR
    ../../configure --target-list=$t-softmmu
    make -j2
done;
