from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
   return render(request, "index.html")

def exhibit(request, year=None, letter=None):
   event_type = 'exhibit'
   event_title = 'exhibits'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def festival(request, year=None, letter=None):
   event_type = 'festival'
   event_title = 'festivals'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def workshop(request, year=None, letter=None):
   event_type = 'workshop'
   event_title = 'workshops'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def talk(request, year=None, letter=None):
   event_type = 'talk'
   event_title = 'talks'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def event(request, year=None, letter=None):
   event_type = 'event'
   event_title = 'events'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def residency(request, year=None, letter=None):
   event_type = 'residency'
   event_title = 'residencies'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def misc(request, year=None, letter=None):
   event_type = 'misc'
   event_title = 'misc'
   year_range = range(2008,2020)
   alpha_range1 = [chr(i) for i in range(ord('A'),ord('M')+1)]
   alpha_range2 = [chr(i) for i in range(ord('N'),ord('Z')+1)]
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)
   if letter is not None:
       events = events.filter(title__startswith=letter)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
        'alpha_range1': alpha_range1,
        'alpha_range2': alpha_range2,
    }
   return render(request, "general_event.html", context=context)

def radio(request):
   return render(request, "radio.html")
