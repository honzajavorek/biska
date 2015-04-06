# -*- coding: utf-8 -*-
from app import index
from django.conf import settings

from django.contrib import admin
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       (r'^$', index),
                       url(r'^admin/', include(admin.site.urls)))

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )