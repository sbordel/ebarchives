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
    path('exhibition', views.exhibition, name='exhibitions'),
    re_path('^exhibition/(?P<year>[0-9]{4})/$', views.exhibition, name='exhibitions'),
    re_path('^exhibition/(?P<letter>[A-Z]{1})/$', views.exhibition, name='exhibitions'),
    re_path('^exhibition/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.exhibition, name='exhibitions'),
    path('collaboration', views.collaboration, name='collaborations'),
    re_path('^collaboration/(?P<year>[0-9]{4})/$', views.collaboration, name='collaborations'),
    re_path('^collaboration/(?P<letter>[A-Z]{1})/$', views.collaboration, name='collaborations'),
    re_path('^collaboration/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.collaboration, name='collaborations'),
    path('salon_data', views.salon_data, name='salon_data'),
    re_path('^salon_data/(?P<year>[0-9]{4})/$', views.salon_data, name='salon_data'),
    re_path('^salon_data/(?P<letter>[A-Z]{1})/$', views.salon_data, name='salon_data'),
    re_path('^salon_data/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.salon_data, name='salon_data'),
    path('sight_sound', views.sight_sound, name='sight_sound'),
    re_path('^sight_sound/(?P<year>[0-9]{4})/$', views.sight_sound, name='sight_sound'),
    re_path('^sight_sound/(?P<letter>[A-Z]{1})/$', views.sight_sound, name='sight_sound'),
    re_path('^sight_sound/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.sight_sound, name='sight_sound'),
    path('workshop', views.workshop, name='workshops'),
    re_path('^workshop/(?P<year>[0-9]{4})/$', views.workshop, name='workshops'),
    re_path('^workshop/(?P<letter>[A-Z]{1})/$', views.workshop, name='workshops'),
    re_path('^workshop/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.workshop, name='workshops'),
    path('radio', views.radio, name='radio'),
    re_path('^radio/(?P<year>[0-9]{4})/$', views.radio, name='radio'),
    path('talk', views.talk, name='talk'),
    re_path('^talk/(?P<year>[0-9]{4})/$', views.talk, name='talks'),
    re_path('^talk/(?P<letter>[A-Z]{1})/$', views.talk, name='talks'),
    re_path('^talk/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.talk, name='talks'),
    path('event', views.event, name='events'),
    re_path('^event/(?P<year>[0-9]{4})/$', views.event, name='events'),
    re_path('^event/(?P<letter>[A-Z]{1})/$', views.event, name='events'),
    re_path('^event/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.event, name='events'),
    path('residence', views.residence, name='residencies'),
    re_path('^residence/(?P<year>[0-9]{4})/$', views.residence, name='residencies'),
    re_path('^residence/(?P<letter>[A-Z]{1})/$', views.residence, name='residencies'),
    re_path('^residence/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.residence, name='residencies'),
    path('meetup', views.meetup, name='meetups'),
    re_path('^meetup/(?P<year>[0-9]{4})/$', views.meetup, name='meetups'),
    re_path('^meetup/(?P<letter>[A-Z]{1})/$', views.meetup, name='meetups'),
    re_path('^meetup/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.meetup, name='meetups'),
    path('e/<int:pk>', views.event_details, name='event_details'),
]
