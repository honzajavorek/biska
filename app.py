# -*- coding: utf-8 -*-
'''
Run this with $ python app.py runserver and go to http://localhost:8000/
'''
from django.shortcuts import render
import os, sys

# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

# SETTINGS
DEBUG = TEMPLATE_DEBUG = True
ROOT_URLCONF = 'urls' # kde jsou nadefinovane adresy
DATABASES = { # definice kde je sqlite databaze
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(here('.'), 'db.sqlite3'),
    }
}
TEMPLATE_DIRS = (here('.'), )
SECRET_KEY = '...'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
)

# VIEW
def index(request):
    return render(request, 'index.html')


if __name__ == '__main__':
    # set the ENV
    os.environ['DJANGO_SETTINGS_MODULE'] = me
    sys.path += (here('.'),)
    # run the development server
    from django.core import management

    management.execute_from_command_line()
