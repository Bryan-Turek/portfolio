from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.list, name='post_list'),
                       url(r'^(?P<post_slug>[\w\-]+)$', views.post, name='post_slug'),
                       url(r'^(?P<post_slug>[\w\-]+)/comments/$', views.comments, name='post_comments')
)
