from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from sfv.views import hello
from sfv.views import login
from sfv.views import New_story
from sfv.views import redirect_to_stories
from sfv.views import stories
from sfv.views import User_stories
from sfv.views import User_story

from django.contrib import admin

from allauth.account.views import logout

admin.autodiscover()

urlpatterns = patterns(
    '',
    # admin
    url(r'^admin/?', include(admin.site.urls)),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('hello'))),
    url(r'^hello/?$', hello, name='hello'),
    url(r'^login/?$', login, name='login'),
    url(r'^stories/?$', stories, name='stories'),
    url(r'^logout/?$', logout, name='logout'),
    url(r'^story/?$', New_story),
    url(r'^story/(?P<slug>[-\w]+)/?$', redirect_to_stories),
    url(r'^(?P<username>[-\w]+)/?$', User_stories),
    url(r'^(?P<username>[-\w]+)/story/(?P<slug>[-\w]+)/?$', User_story),

    # Social urls:
    (r'^accounts/', include('allauth.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
