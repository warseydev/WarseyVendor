#!/bin/bash

echo "Building Warsey's Vendor System."
mkdir ~/warseyapps-files
mkdir ~/warseyapps-files/warseyvendor
if [ ! -d "~/warseyapps-files/warseyvendor/invitecodes" ]; then
    mv src/appdata/* ~/warseyapps-files/warseyvendor
    mkdir ~/warseyapps-files/warseyvendor/invitecodes
fi
docker-compose up -d