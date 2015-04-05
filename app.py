# -*- coding: utf-8 -*-
'''
Spustit jako $ python app.py a jit na http://localhost:8000/
'''
from django.conf import settings
from django.conf.global_settings import MIDDLEWARE_CLASSES, TEMPLATE_CONTEXT_PROCESSORS
from django.shortcuts import render, redirect
import os, sys

# tento modul
me = os.path.splitext(os.path.split(__file__)[1])[0]
# najdi tento adresar
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


# VIEW
def index(request):
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth.views import login

    return login(request, template_name='index.html')


if __name__ == '__main__':
    # SETTINGS
    inline_sett = {
        # definice kde je sqlite databaze
        'DATABASES': {'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(here('.'), 'db.sqlite3'),
        }},
        'INSTALLED_APPS': (
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
        ),
        'MIDDLEWARE_CLASSES':
            MIDDLEWARE_CLASSES + ('django.contrib.sessions.middleware.SessionMiddleware',
                                  'django.contrib.auth.middleware.AuthenticationMiddleware',
                                  'django.contrib.messages.middleware.MessageMiddleware'),
        'TEMPLATE_CONTEXT_PROCESSORS':
            TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request',)
    }

    settings.configure(
        **dict(inline_sett,
               DEBUG=True,
               # DEBUG=False,
               # ALLOWED_HOSTS=['*'],
               LANGUAGES=(('cs', ''),),
               LANGUAGE_CODE='cs',
               USE_I18N=True,
               ROOT_URLCONF='urls',
               MEDIA_ROOT=here('.'),
               TEMPLATE_DIRS=(here('.'), ),
               LOGIN_REDIRECT_URL='/',
               SECRET_KEY='...')
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

