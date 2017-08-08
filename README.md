# Git Commands
==============
# On windows, open up git bash to do the following commands

# Always run the pull command first
git pull


# To add files you have updated 
git add .

# To commit to your local repository
git commit -m "Adding updates to existing files"

# To push the changes to the master branch on git
git push origin master


# finalproject

# Documenting steps to start a Django project
### FOR WINDOWS USERS, use python
### FOR Mac OS X Users, use python3

#Use the correct version of Python to use Django, if you are on windows use python instead of python3:
"python3 --version"

Create a virtual environmnet with this command, if you are on windows use python instead of python3:
"python3 -m venv huddleupvenv"

Activate the virtual environmetn with this command:
"source huddleupvenv/bin/activate"


Install Django
"pip install django~=1.10.0"


Start your project
"django-admin startproject huddleupsite"

Start your app
"python3 manage.py startapp huddleupapp"

In order to create the default databases that Django supports for users, groups you need to add the tables
"python3 manage.py migrate"

Create your super user
"python3 manage.py createsuperuser"

Run your server
"python3 manage.py runserver"


In order to login go to the following page:
"http://127.0.0.1:8000/admin/"


To get your list of users when the server is running go to the following page:
http://127.0.0.1:8000/admin/auth/user/

To get your list of groups when the server is running go to the following page:
http://127.0.0.1:8000/admin/auth/group/




