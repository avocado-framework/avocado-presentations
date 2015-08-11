#!/bin/bash -e

# Configures ~/public_html so that apache serves the user's content
# Must be run as the user that intends to serve avocado results

if [ ! -d ~/public_html ]; then
    mkdir ~/public_html
fi
setfacl -m g:apache:x ~/
setfacl -R -m g:apache:rx ~/public_html
setfacl -d -m g:apache:rx ~/public_html


if [ ! -d ~/avocado ]; then
    mkdir ~/avocado
fi
setfacl -m g:apache:rx ~/avocado
cp -ru ~/avocado/job-results ~/public_html/ && rm -fr ~/avocado/job-results
ln -s ~/public_html/job-results ~/avocado/
