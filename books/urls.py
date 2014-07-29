from django.conf.urls import patterns

from django.contrib import admin

from django.conf.urls import patterns, url, include
from rest_framework import routers
from books import views

import logging


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)



