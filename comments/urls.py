from django.conf.urls import patterns, url
from comments import views

urlpatterns = patterns('',
                       url(r'^$', views.list, name='comment_list')
)
