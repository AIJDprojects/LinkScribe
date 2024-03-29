#!/bin/bash

sudo cd Backend/

echo "install poetry"
pip install fastapi
pip install uvicorn
pip install numpy
pip install scikit-learn
pip install bs4
pip install requests
pip install imgkit

sudo apt-get update
sudo apt-get install wkhtmltopdf -y

