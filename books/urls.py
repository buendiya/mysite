from django.conf.urls import patterns

from django.contrib import admin

import logging
try:
    from mysite.views import search_form, search
except Exception, e:
    logging.warning(e)

admin.autodiscover()


urlpatterns = patterns('',
    (r'^search-form/$', search_form),
    (r'^search/$', search),
)
