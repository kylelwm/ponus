from django.conf.urls import patterns, url

from modules import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^modulelist', views.modulelist, name='modulelist'),
	url(r'^addmodule', views.addmodule, name='addmodule'),
	url(r'^sorttable', views.sorttable, name='sorttable'),
	url(r'^update', views.update, name='update'),

)