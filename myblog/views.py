from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category,Tag,Post
from django.contrib.auth import authenticate, login,logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


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
    else:
        return HttpResponse('<h1>Error</h1>')    
  
def UserLogout(request):
    logout(request)
    url=reverse("index")
    return HttpResponseRedirect(url)

def UserRegister(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    user = User.objects.create_user(username, email, password)
    if user is not None:
        url=reverse("index")
        return HttpResponseRedirect(url)
    return HttpResponse('<h1>Error</h1>')