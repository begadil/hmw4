from django.conf.urls import patterns, url

from blogapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>\d+)/$', views.detail, name='detail'),
)
