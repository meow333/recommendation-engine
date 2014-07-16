from django.conf.urls import patterns, url

from votes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<votes_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<votes_id>\d+)/votes/$', views.details, name='details'),
    url(r'^(?P<votes_id>\d+)/results/$', views.result, name='result'),
)
