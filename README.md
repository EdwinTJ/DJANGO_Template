# DJANGO_Template

### Introduction

This template is designed to simplify the setup process, allowing you to dive straight into the core aspects of your project.

### Clone Repository

Clone the repository:

    $ git clone git@github.com:EdwinTJ/DJANGO_Template.git {{project_name}}
    $ cd {{project_name}}
    
Then run poetry

    $ poetry install
    $ cd _project
    $ poetry shell
    $ python manage.py runserver
    
### Organization
* Organization
    * The folder _project 
        * Is the project core
        * Were we deleted some settings
    * The app folder 
        * views, template, static 
* Template
    * Password Generator
        * This template contains the program password generator  based on the example demonstrated in the module 2.2 videos

### Deleted Settings
* INSTALLED_APPS
    *  django.contrib.admin
    *  django.contrib.auth
    *  django.contrib.sessions
    *  django.contrib.messages
* MIDDLEWARE
    * django.contrib.sessions.middleware.SessionMiddleware
    * django.middleware.csrf.CsrfViewMiddleware
    * django.contrib.auth.middleware.AuthenticationMiddleware
    * django.contrib.messages.middleware.MessageMiddleware
* TEMPALTES `context_processors`
    * django.contrib.auth.context_processors.auth
    * django.contrib.messages.context_processors.messages

Please feel free to use the repository as a template to make it easier. If you find something wrong, let me know.

Hope it helps
