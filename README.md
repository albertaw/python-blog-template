
## Installation / Setup
Download code from github

### Mac

__Install python__
Check for Python: ==============
Download: [https://www.python.org/downloads/]
This project uses Python 2
Confirm installation: `python --version`

__Install Django__
Check for Django: =================
?Install pip: [https://pip.pypa.io/en/latest/installing/#install-pip]
Install virtualenv. virtualenv creates an isolated python environment 
where your project's dependencies will be contained. This is preferred
 to installing packages in the global site-packages directory.
 
`pip install virtualenv`

From a terminal window enter the command:
`sudo pip install Django`
This project uses Django 1.10.  If you need to upgrade enter the 
command===========
Confirm installation
`bash
python
>>> import django
>>> django.get_version()
`
### Running locally
In myproject/settings.py set TIME_ZONE to your time zone
Create the tables for the database that the installed apps use: 
`python manage.py migrate`

To run server, change into the directory where the manage.py file lives
and in your terminal type the command:
`python manage.py runserver`
Then in browser type: http://127.0.0.1:8000


### Windows

## Project Architecture / Directory Structure
src - Main project folder
src/myproject - the python package for the project
src/myproject/__init__.py - An empty file that tells Python that this directory should be considered a Python package.
src/myproject/setings.py - configuration for Django project, module level variables



## API

