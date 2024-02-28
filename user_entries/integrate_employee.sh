#!/bin/bash

#system integration step
python system_integration.py

#create user data package
python create_package_json.py

#copy package file into Houdini
cp packages/company_vars.json C:/Users/fiona/Documents/houdini20.0/packages

echo "All steps done!"