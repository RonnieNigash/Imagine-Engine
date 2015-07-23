from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns("webUI.views", url(r'^input/$', 'input', name = 'input'),)
#urlpatterns = [ url(r'^$', views.index, name = 'index'), ]
