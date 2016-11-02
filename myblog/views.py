from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category,Tag


def index(request):
    categories = Category.objects.all()
    tags=Tag.objects.all()
    return render(request, "index.html", {'categories': categories,'tags':tags})



