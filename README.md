HR Automation Backend
=====================

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
 - `./manage.py runserver`
