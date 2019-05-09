"""ebarchivesweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ebarchivesweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('acknowledgment', views.acknowledgment, name='acknowledgment'),
    path('exhibitions', views.exhibition, name='exhibitions'),
    re_path('^exhibitions/(?P<year>[0-9]{4})/$', views.exhibition, name='exhibitions'),
    re_path('^exhibitions/(?P<letter>[A-Z]{1})/$', views.exhibition, name='exhibitions'),
    re_path('^exhibitions/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.exhibition, name='exhibitions'),
    path('collaborations', views.collaboration, name='collaborations'),
    re_path('^collaborations/(?P<year>[0-9]{4})/$', views.collaboration, name='collaborations'),
    re_path('^collaborations/(?P<letter>[A-Z]{1})/$', views.collaboration, name='collaborations'),
    re_path('^collaborations/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.collaboration, name='collaborations'),
    path('salon_data', views.salon_data, name='salon_data'),
    re_path('^salon_data/(?P<year>[0-9]{4})/$', views.salon_data, name='salon_data'),
    re_path('^salon_data/(?P<letter>[A-Z]{1})/$', views.salon_data, name='salon_data'),
    re_path('^salon_data/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.salon_data, name='salon_data'),
    path('sight_sound', views.sight_sound, name='sight_sound'),
    re_path('^sight_sound/(?P<year>[0-9]{4})/$', views.sight_sound, name='sight_sound'),
    re_path('^sight_sound/(?P<letter>[A-Z]{1})/$', views.sight_sound, name='sight_sound'),
    re_path('^sight_sound/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.sight_sound, name='sight_sound'),
    path('workshops', views.workshop, name='workshops'),
    re_path('^workshops/(?P<year>[0-9]{4})/$', views.workshop, name='workshops'),
    re_path('^workshops/(?P<letter>[A-Z]{1})/$', views.workshop, name='workshops'),
    re_path('^workshops/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.workshop, name='workshops'),
    path('radio', views.radio, name='radio'),
    re_path('^radio/(?P<year>[0-9]{4})/$', views.radio, name='radio'),
    path('talks', views.talk, name='talk'),
    re_path('^talks/(?P<year>[0-9]{4})/$', views.talk, name='talks'),
    re_path('^talks/(?P<letter>[A-Z]{1})/$', views.talk, name='talks'),
    re_path('^talks/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.talk, name='talks'),
    path('events', views.event, name='events'),
    re_path('^events/(?P<year>[0-9]{4})/$', views.event, name='events'),
    re_path('^events/(?P<letter>[A-Z]{1})/$', views.event, name='events'),
    re_path('^events/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.event, name='events'),
    path('residencies', views.residence, name='residencies'),
    re_path('^residencies/(?P<year>[0-9]{4})/$', views.residence, name='residencies'),
    re_path('^residencies/(?P<letter>[A-Z]{1})/$', views.residence, name='residencies'),
    re_path('^residencies/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.residence, name='residencies'),
    path('meetups', views.meetup, name='meetups'),
    re_path('^meetups/(?P<year>[0-9]{4})/$', views.meetup, name='meetups'),
    re_path('^meetups/(?P<letter>[A-Z]{1})/$', views.meetup, name='meetups'),
    re_path('^meetups/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.meetup, name='meetups'),
    path('e/<int:pk>', views.event_details, name='event_details'),
]
