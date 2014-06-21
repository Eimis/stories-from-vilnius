from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from sfv.views import landing, test, logout, restricted, redirect_to_login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	#App urls:
    url(r'^$', landing),
    url(r'^test/$', test),
    url(r'^test/restricted/$', restricted),
    url(r'^accounts/login/$', redirect_to_login),
    url(r'^logout/$', logout),

    #Facebook urls:
    (r'^facebook/', include('django_facebook.urls')),


    #admin
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
