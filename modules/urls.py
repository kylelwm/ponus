from django.conf.urls import patterns, url

from modules import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^modulelist', views.modulelist, name='modulelist'),
	url(r'^testsearch', views.testsearch, name='testsearch'),
	url(r'^sorttable', views.sorttable, name='sorttable'),
)