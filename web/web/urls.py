from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.conf import settings

from main.views import ImageIndexView

from django.contrib import admin
admin.autodiscover()

from main.views import ImageView, DetailView

urlpatterns = patterns('',
		url(r'^$', ImageIndexView.as_view(), name = 'home'),

		url(r'^upload/', ImageView.as_view(), name = 'image_upload'),

		url(r'^uploaded/(?P<pk>\d+)/$', DetailView.as_view(), name = 'image'),

		url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
