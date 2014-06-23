from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from sfv.views import landing, Login, logout, redirect_to_login, Stories, User_stories, New_story, User_story

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	#App urls:
    #url(r'^$', landing),
    url(r'^$', Login),
    url(r'^stories/$', Stories), #all stories
    url(r'^logout/$', logout),
    url(r'^story/$', New_story),
    url(r'^(?P<username>[-\w]+)/$', User_stories),
    url(r'^(?P<username>[-\w]+)/(?P<slug>[-\w]+)/$', User_story),
    url(r'^accounts/login/$', redirect_to_login),

    #Facebook urls:
    (r'^facebook/', include('django_facebook.urls')),


    #admin
    url(r'^site/admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
