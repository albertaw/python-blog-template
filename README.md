
## Installation (Mac)

#### I. Download code from github  
```bash
git clone git@github.com:albertaw/python-blog-template.git
```
cd into the directory python-blog-template

#### II. Install python
This project uses Python 2.7.8.  Check that you have Python with the command
`python --version`.  If not download python here: [www.python.org/downloads]
Confirm the installation by entering the command `python --version`.

### III. Install Django
This project users Django 1.10.1.  Check that you have Django by entering the
following commands in the terminal:
```bash
python
>>> import django
>>> django.get_version()
```

If you you do not have Django installed you can download it using pip.
To upgrade pip type the command: 
```bash
pip install -U pip
```
If you need to get pip run the following commands: 
```bash
python get-pip.py
```
Next you can install django with:
```bash
sudo pip install Django
```

#### IV. Start the app
In myproject/settings.py set TIME_ZONE to your time zone.
Create the tables for the database that the installed apps use: 
```bash
python manage.py migrate
```
To start the server, change into the directory where the manage.py file lives
and in your terminal type the command:
```bash
python manage.py runserver
```
Then in your browser go to: [127.0.0.1:8000]


## API

GET /posts  
GET /posts/:post_id  
POST /posts/new  
GET /users  
GET /users/:user_id  
GET /auth/  
POST /auth/  
GET /auth/logout  
POST /auth/logout  
GET /accounts/register  
GET /dashboard  
POST /dashboard  

