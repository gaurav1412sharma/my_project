#!/usr/bin/env bash

# Exit on first error
set -e

# Install node dependencies and build the React app
echo "Building React app..."
cd CSIR_NPL/build
yarn install
yarn build

# Move back to the Django root directory
cd ../..

# Collect static files for Django
echo "Collecting static files..."
python manage.py collectstatic --noinput
