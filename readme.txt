
# My_Django_App
pip install django
django-admin startproject projectname
cd projectname

 Create a new Django app
python manage.py startapp appname

 Configure the database
By default, Django uses SQLite as the database backend. If you want to use a different database, 
update the database settings in the settings.py file located in your project directory. 
Django supports various databases, such as PostgreSQL, MySQL, and Oracle.


 Define your models
Models in Django represent the structure of your data. Open the models.py file within your app directory 
and define your models using Python classes.Each attribute of a model represents a database field.

: Create database tables
1ST: python manage.py makemigrations
After complete table query : python manage.py migrate

: Run the development server
python manage.py runserver



--Sari logical cheeze views me hotii ha
--- routing urls me hotii ha

add this in url file
from django.conf.urls.static import static

FOR CSS

For css link static/css
In html we write 
{%  load static %}
<Doctype HTML>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
In settings.py

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

add in settins in templates 
'DIRS': [BASE_DIR / 'templates'],


FOR Image
HTML img
 {% load static %}
    <img src="{% static 'img/1.jpeg' %}" alt="My Image">

CSS image
background-image: url("../img/1.jpg");






make database 

python manage.py makemigrations

python manage.py migrate 

for the datatbase add in settings project name e.g(my_project) in instaled_apps

from my_project.models import * in view file




