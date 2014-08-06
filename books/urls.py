from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import routers
from books.views import BookListView, UserViewSet, GroupViewSet



admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^books/$', BookListView.as_view()),
)



