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
    path('exhibit', views.exhibit, name='exhibit'),
    path('festival', views.festival, name='festival'),
    re_path('^workshop/(?P<year>[0-9]{4})/$', views.workshop, name='workshop'),
    re_path('^workshop/(?P<letter>[A-Z]{1})/$', views.workshop, name='workshop'),
    re_path('^workshop/(?P<year>[0-9]{4})/(?P<letter>[A-Z]{1})/$', views.workshop, name='workshop'),
    path('radio', views.radio, name='radio'),
    path('talk', views.talk, name='talk'),
    path('event', views.event, name='event'),
    path('misc', views.misc, name='misc'),
]
