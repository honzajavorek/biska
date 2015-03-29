# -*- coding: utf-8 -*-
from app import index

from django.contrib import admin
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       (r'^$', index),
                       url(r'^admin/', include(admin.site.urls)))

