from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category,Tag,Post
from django.contrib.auth import authenticate, login,logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    categories = Category.objects.all()
    posts= Post.objects.all()
    tags=Tag.objects.all()
    return render(request, "index.html", {'categories': categories,'tags':tags,'posts':posts})

def UserLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        url=reverse("index")
        return HttpResponseRedirect(url)
  
def UserLogout(request):
    logout(request)
    url=reverse("index")
    return HttpResponseRedirect(url)