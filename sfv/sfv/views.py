
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sfv.forms import StoryForm
from sfv.models import Story


def hello(request):
    return render(request, "hello.html", {})

def login(request):
    user = request.user
    return render(request, "login.html", {'user': user})


@login_required(redirect_field_name=None)
# @facebook_required(scope='publish_stream')
# @csrf_protect
def stories(request):
    '''
    A view which displays a map with ALL users Stories.
    Some recent stories will be displayed under the map.
    '''
    form = StoryForm(request, request.POST, request.FILES)
    return render(request, "stories.html", {'form': form})


@login_required(redirect_field_name=None)
def User_stories(request, username):
    '''
    A view to list stories submitted by particular User (username extracted
    from URL).
    '''
    # user = FacebookCustomUser.objects.get(username=username)
    user_stories = Story.objects.filter(user=user)
    return render(request, "user_stories.html", {'user_stories': user_stories})


@login_required(redirect_field_name=None)
def User_story(request, username, slug):
    '''
    A view which displays particular User's story ('name/slug')
    '''

    # user = FacebookCustomUser.objects.get(username=username)
    story = Story.objects.get(user=user, slug=slug)
    share_link = request.get_full_path()
    form = StoryForm(request, instance=story)
    return render(request, "user_story.html", {
        'story': story,
        'share_link': share_link,
        'form': form
    })


@login_required(redirect_field_name=None)
# @facebook_required(scope='publish_stream')
# @csrf_protect
def New_story(request):
    '''
    A view to add new Story from Vilnius
    '''
    user = request.user
    if request.method == 'POST':
        form = StoryForm(request, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # graph.set('me/feed', message='Helo')
            return HttpResponseRedirect(request.path)
        else:
            form = StoryForm(request, request.POST, request.FILES)
        return render(request, "new_story.html", {'form': form})
    else:
        form = StoryForm(request)  # request.get
        try:
            # lastest:
            # story = Story.objects.all().filter(
                # user=user
            # ).order_by('-date')[0]
            story = Story.objects.filter(user=user).order_by('-date')[0]
            return render(request, "new_story.html", {
                'form': form,
                'story': story
            })
        except IndexError:  # no Stories submitted yet
            pass
    return render(request, "new_story.html", {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(redirect_field_name=None)
def redirect_to_stories(request, slug):
    return HttpResponseRedirect('/stories/')

# TODO: User vs current_user (User_stories)
# username = slugintas fb vardas pavarde
# landing page = img
