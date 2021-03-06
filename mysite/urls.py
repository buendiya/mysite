from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello, current_datetime, hours_ahead, AboutView
from django.views.generic import TemplateView
import logging
from rest_framework.tests.test_serializer import BookSerializer
try:
    from books.views import search, contact, thanks, display_meta
except Exception, e:
    logging.warning(e)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('books.urls')),
    url(r'^', include('snippets.urls')),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
#    (r'^search-form/$', search_form),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^contact/thanks/$', thanks),
    (r'^display_meta/$', display_meta),
    url(r'^about/', AboutView.as_view()),
)
