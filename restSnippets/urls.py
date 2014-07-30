from django.conf.urls import patterns, url

urlpatterns = patterns('restSnippets.views',
    url(r'^', 'snippet_list'),
    url(r'^(?P<pk>[0-9]+)/$', 'snippet_detail'),
)