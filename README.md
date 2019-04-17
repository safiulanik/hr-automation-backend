HR Automation - Backend
=====================

Features
--------
 - Self registration with roles ('engineer', 'manager', 'hr')
 - User login
 - Track requests

For Engineer role:
 - Create new request
 - View all requests of current user
 - Update/Delete existing requests

For HR role:
 - View all requests made by all users
 - Process requests
 - Create new request
 - Update/Delete existing requests

For manager:
 - View requests with hr_reviewed status
 - Process requests
 - Create new request
 - Update/Delete requests

Installation
------------
Recommended python version: 3.6+

Run the following commands in terminal to run the project:

 - `git clone https://github.com/safiulanik/hr-automation-backend.git`
 - `cd hr-automation-backend`
 - `python3 -m venv venv`
 - `source venv/bin/activate`
 - `cd hrautomation`
 - `pip install -r requirements.txt`
 - `cd hrautomation`
 - Add `local_settings.py` with necessary variables; Demo file:

 ```
 CORS_ORIGIN_WHITELIST = '*'
 ALLOWED_HOSTS = ['localhost:3000','127.0.0.1']
 EMAIL_DOMAIN = 'gmail'
 EMAIL_DOMAIN_EXTENSION = 'com'

 ```

 - `cd ..`
 - `./manage.py migrate`
 - `./manage.py runserver`
 

To run the tests, move to the hrautomation folder and run the following command:
 - `python manage.py test hrautomationapi.tests`