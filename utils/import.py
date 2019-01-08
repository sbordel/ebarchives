#!/usr/bin/python3
# -*- coding: utf-

import os, csv, sys, django, string

sys.path.append("/home/tvaz/Hacking/ebarchives/ebarchivesweb")
os.environ["DJANGO_SETTINGS_MODULE"] = "ebarchivesweb.settings"
django.setup()

from ebarchivesweb.models import *

path = "/home/tvaz/Hacking/ebarchives/CSV"
os.chdir(path)

event_type = EventType.objects.get(type="exhibit")
print("EVENT TYPE: " + str(event_type))

with open('exhibits.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        p = Event(title=row['TITLE_EN'],
                  title_fr=row['TITLE_FR'],
                  description=row['DESCRIPTION_EN'],
                  description_fr=row['DESCRIPTION_FR'],
                  type=event_type,
                  year=row['YEAR'],
                  comment=row['COMMENTS'])
        print("EVENT TITLE:" + str(p))
        p.save()

        # ARTISTS MANYTOMANY
        if row['ARTISTS']:
            artists = row['ARTISTS'].split("\n")
            print(artists)
            for a in artists:
                if a:
                    print("GETTING ARTIST: " + a)
                    a_obj = Artist.objects.get(name=str.lower(a))
                    if a_obj:
                        p.artist.add(a_obj)
            p.save()

        # MEDIA MANYTOMANY

        # TYPE FOREIGNKEY
