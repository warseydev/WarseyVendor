#!/bin/bash

echo "Building Warsey's Vendor System."
mkdir ~/warseyapps-files
mkdir ~/warseyapps-files/warseyvendor
cp -r src/appdata/* ~/warseyapps-files/warseyvendor
mkdir ~/warseyapps-files/warseyvendor/invitecodes
docker-compose up -d