from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
   return render(request, "index.html")

def exhibit(request):
   return render(request, "exhibit.html")

def festival(request):
   return render(request, "festival.html")

def workshop(request, year=None, letter=None):
   workshops = Event.objects.filter(type__type__exact='workshop')
   if year is not None:
       workshops = workshops.filter(year=year)
   if letter is not None:
       workshops = workshops.filter(title__startswith=letter)

   context = {
        'workshops': workshops,
    }
   return render(request, "workshop.html", context=context)

def radio(request):
   return render(request, "radio.html")

def talk(request):
   return render(request, "talk.html")

def event(request):
   return render(request, "event.html")

def misc(request):
   return render(request, "misc.html")
