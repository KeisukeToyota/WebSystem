from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<id>\d+)/post_comment', views.post_comment, name='post_comment'),
    url(r'(?P<id>\d+)/$', views.blog_index, name='blog'),
]
