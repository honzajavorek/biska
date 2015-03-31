# -*- coding: utf-8 -*-
'''
Spustit jako $ python app.py a jit na http://localhost:8000/
'''
from django.conf import settings
from django.conf.global_settings import MIDDLEWARE_CLASSES, TEMPLATE_CONTEXT_PROCESSORS
from django.shortcuts import render
import os, sys

# tento modul
me = os.path.splitext(os.path.split(__file__)[1])[0]
# najdi tento adresar
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


# VIEW
def index(request):
    return render(request, 'index.html')



if __name__ == '__main__':
    # SETTINGS
    inline_sett = {
        'DATABASES': {  # definice kde je sqlite databaze
                        'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': os.path.join(here('.'), 'db.sqlite3'),
                        }
                        },
        'INSTALLED_APPS': (
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
        ),
        'MIDDLEWARE_CLASSES': MIDDLEWARE_CLASSES + ('django.contrib.sessions.middleware.SessionMiddleware',
                                                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                                                    'django.contrib.messages.middleware.MessageMiddleware'),
        'TEMPLATE_CONTEXT_PROCESSORS': TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request',)
    }

    settings.configure(
        **dict(inline_sett,
               DEBUG=True,
               ROOT_URLCONF='urls',
               TEMPLATE_DIRS=(here('.'), ),
               SECRET_KEY='...')
    )

    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], 'runserver'])

