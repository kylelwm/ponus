from django.conf.urls import patterns, url

from modules import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^modulelist', views.modulelist, name='modulelist'),
	url(r'^addmodule', views.addmodule, name='addmodule'),
	url(r'^sorttable', views.sorttable, name='sorttable'),
	url(r'^update', views.update, name='update'),
	url(r'^newsearch', views.newsearch, name='newsearch'),
	url(r'^home', views.home, name='home'),
	url(r'^main', views.main, name='main'),
	url(r'^newmodule', views.newmodule, name='newmodule'),
	url(r'^deletemodule', views.deletemodule, name='deletemodule'),
	url(r'^palette', views.palette, name='palette'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),

)