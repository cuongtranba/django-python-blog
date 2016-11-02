from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category 

def index(request):
    categories=Category.objects.all()
    return render(request,"index.html",{'categories':categories})



    