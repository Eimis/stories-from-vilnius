
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.sites.models import Site
#from django_facebook.decorators import facebook_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sfv.forms import StoryForm
from sfv.models import Story
from django.http import HttpResponse, HttpResponseRedirect

from django_facebook.api import get_persistent_graph
from open_facebook import OpenFacebook
from open_facebook.api import FacebookAuthorization
from sfv import settings
from django_facebook.models import FacebookCustomUser
#from django.views.decorators.csrf import csrf_protect


def landing(request):
	return render(request, "landing.html", {})

def Login(request):
	return render(request, "login.html", {})




@login_required(redirect_field_name=None)
#@facebook_required(scope='publish_stream')
#@csrf_protect
def Stories(request):
    '''
    A view which displays a map with ALL users Stories.
    Some recent stories will be displayed under the map.
    '''
    return render(request, "stories.html", {})


@login_required(redirect_field_name=None)
def User_stories(request, username):
    '''
    A view to list stories submitted by particular User (username extracted from URL).
    If this User is currently logged in, he will be able to add his own Story.
    '''
    try: # query all users
        FacebookCustomUser.objects.get(username = username)
    except FacebookCustomUser.DoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, "user_stories.html", {})

@login_required(redirect_field_name=None)
def User_story(request, slug):
    '''
    A view which displays particular User's story ('name/slug')
    '''
    return render(request, "user_story.html", {})


@login_required(redirect_field_name=None)
#@facebook_required(scope='publish_stream')
#@csrf_protect
def New_story(request):
    '''
    A view to add new Story from Vilnius
    '''
    user = request.user
    if request.method == 'POST':
        form = StoryForm(request, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #graph.set('me/feed', message='Helo')
            return HttpResponseRedirect(request.path)
        return render(request, "restricted.html", {'form' : form})
    else:
        form = StoryForm(request) # request.get
        try:
            story = Story.objects.all().filter(user = user).order_by('-date')[0] #lastest
            return render(request, "new_story.html", {'form' : form, 'story' : story})
        except IndexError:
            pass
    return render(request, "new_story.html", {'form' : form,})





def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def redirect_to_login(request):
	return HttpResponseRedirect('/')

#TODO: User vs current_user (User_stories)