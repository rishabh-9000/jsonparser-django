# JSON Parser using Django

JSON parser from api url made using Django

## Installation

Install pip first
```bash
sudo apt-get install python3-pip
```
Then install virtualenv using pip
```bash
pip install virtualenv
```
Now create virtual environment
```bash
virtualenv envname

*To create virtual environment with Python 3 as default
virtualenv -p python3 envname
```
Activate the virtual environment
```bash
source envname/bin/activate
```

## Project Setup

Cloning the project from github
```bash
git clone https://github.com/rishabh-9000/jsonparser-django.git
cd jsonparser-django
```
Install Django and requirements
```bash
pip install -r requirements.txt
```
To run the server
```bash
python manage.py runserver
```