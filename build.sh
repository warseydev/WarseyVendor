#!/bin/bash

echo "Building Warsey's Vendor System."
cp -r src/appdata/* ~/warseyapps-files/warseyvendor
docker-compose up -d