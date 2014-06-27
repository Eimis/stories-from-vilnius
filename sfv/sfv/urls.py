from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from sfv.views import landing, Login, logout, redirect_to_login, redirect_to_stories, Stories, User_stories, User_story, New_story

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	#App urls:
    url(r'^landing/?$', landing),
    url(r'^$', Login),
    url(r'^accounts/login/?$', redirect_to_login),
    url(r'^stories/?$', Stories),
    url(r'^logout/?$', logout),
    url(r'^story/?$', New_story),
    url(r'^story/(?P<slug>[-\w]+)/?$', redirect_to_stories),
    url(r'^(?P<username>[-\w]+)/?$', User_stories),
    url(r'^(?P<username>[-\w]+)/story/(?P<slug>[-\w]+)/?$', User_story),

    #Facebook urls:
    (r'^facebook/', include('django_facebook.urls')),


    #admin
    url(r'^site/admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
