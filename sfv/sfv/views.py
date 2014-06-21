
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.sites.models import Site
from django_facebook.decorators import facebook_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django_facebook.api import get_persistent_graph
from open_facebook import OpenFacebook
from open_facebook.api import FacebookAuthorization



def landing(request):
	return render(request, "landing.html", {})

def test(request):
	return render(request, "test.html", {})




@login_required(redirect_field_name=None)
def restricted(request):
    user = request.user
    graph = get_persistent_graph(request)
    return render(request, "restricted.html", {user : 'user',})


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/test")

def redirect_to_login(request):
	return HttpResponseRedirect('/test/')