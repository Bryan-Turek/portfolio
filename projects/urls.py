from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
                       url(r'^$', views.list, name='project_list'),
                       url(r'^(?P<project_name>[\w\-]+)$', views.project, name='project_name')
)
