#!/bin/bash

echo "Building Warsey's Vendor System."
if [ ! -d "~/warseyapps-files/warseyvendor" ]; then
    mkdir ~/warseyapps-files
    mkdir ~/warseyapps-files/warseyvendor
    mv src/appdata/* ~/warseyapps-files/warseyvendor
    mkdir ~/warseyapps-files/warseyvendor/invitecodes
fi
docker-compose down
docker-compose up -d