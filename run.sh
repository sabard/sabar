#!/bin/bash

if [ $1 == "--docker" ] ; then
    docker build -t sabar_me .
    docker run -d -p 5000:5000 sabar_me
else
    set -a && . ./variables-dev.env && set +a
    gunicorn --bind 0.0.0.0:5000 sabar_me:app

fi
