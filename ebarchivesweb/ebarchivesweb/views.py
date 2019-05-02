from django.shortcuts import render
from django.conf import settings
from .models import *
from os import listdir
from os.path import isfile, join
import imghdr

# Create your views here.

def index(request):
   return render(request, "index.html")

def acknowledgment(request):
   return render(request, "ack.html")

def event_details(request, pk):
   event = Event.objects.get(pk=pk)
   media_list = []
   images_folder = None
   images = None
   
   for m in event.media.all():
       if m.type == 'image':
           images_folder = m.url + '/'
           break
   if images_folder:
       images_path = settings.MEDIA_ROOT + images_folder
       images = [settings.MEDIA_URL+images_folder+f for f in listdir(images_path) if imghdr.what(join(images_path, f))]
   context = { 'event':event, 'images':images }
   return render(request, "event_details.html", context=context)

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

def residence(request, year=None, letter=None):
   event_type = 'residence'
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

def radio(request, year=None):
   event_type = 'radio'
   event_title = 'radio'
   year_range = range(2015,2020)
   events = Event.objects.filter(type__type__exact=event_type)
   if year is not None:
       events = events.filter(year=year)

   context = {
        'events': events,
        'event_title': event_title,
        'event_type': event_type,
        'year_range': year_range,
    }
   return render(request, "radio.html", context=context)

def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Event.objects.filter(title__icontains=query).distinct()
    else:
        results = []
 
    context = {
         'events': results,
     }
    return render(request, "general_event.html", context=context)

