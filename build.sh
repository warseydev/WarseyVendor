#!/bin/bash

echo "WARSEY 2022 (R) - Building Warsey's Vendor System."
DIRECTORY=~/warseyapps-files/warseyvendor
if [ ! -d "$DIRECTORY" ]; then
    mkdir ~/warseyapps-files
    mkdir ~/warseyapps-files/warseyvendor
    mv src/appdata/* ~/warseyapps-files/warseyvendor
    mkdir ~/warseyapps-files/warseyvendor/invitecodes
fi
docker-compose down
docker-compose up --build -d