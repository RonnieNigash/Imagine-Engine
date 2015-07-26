from django.conf.urls import patterns, url
from search import views

urlpatterns = patterns('',
		(r'^$', views.input, name='input'),
)
