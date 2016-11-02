from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import models
# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def Category(request):
    categories=Category.objects.all()
    return render(request,"category.html",{'categories':categories})


    