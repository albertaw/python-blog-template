## Installation (Mac)

#### I. Download code from github  

```bash
git clone git@github.com:albertaw/python-blog-template.git
```

Change into the directory python-blog-template

#### II. Install python
This project uses Python 2.7.8.  Check that you have Python with the command
`python --version`.  If not download python here: www.python.org/downloads
Confirm the installation by entering the command `python --version`.


#### III. Set up a virtual environment
You can use virtualenv to keep your project dependencies isolated. More info here:
[https://virtualenv.pypa.io/en/stable/userguide/]
You can download virtualenv with pip. If you need to get pip run the following commands: 
```bash
python get-pip.py
```

Install virtualenv:
```bash
pip instal virtualenv
```

Create the virtual environment:
```bash
virtualenv venv
```

Activate you virtual environment:
```bash
source venv/bin/activate
```


#### IV. Install project dependencies
```bash
pip install -r requirements.txt
```


#### V. Start the app

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
Then in your browser go to: 127.0.0.1:8000


## API

GET /posts  
returns all posts

GET /posts/:post_id  
returns a post with the id post_id

GET /posts/new  
returns the create new post page

POST /posts/new  
creates a new post

GET /users  
returns all users

GET /users/:user_id  
returns the user with username user_id

GET /auth/  
returns the login page

POST /auth/  
logs in the user

POST /auth/logout  
logs out the user

GET /accounts/register  
returns the registration page
