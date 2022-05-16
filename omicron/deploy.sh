#!/bin/sh

cd /home/flux/programs/project-omicron-frontend/omicron-frontend
git pull
npm install
npm run build
cp -r build/* /var/www/html/static/stuff

cd /home/flux/programs/project-omicron-backend
git pull
pkill daphne
