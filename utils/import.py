#!/usr/bin/python3
# -*- coding: utf-

# ===== SETUP ========
type = 'talk'
csv_file = 'talks.csv'
# ==== END SETUP =====

import os, csv, sys, django, string

sys.path.append("/home/tiago/Hacking/ebarchives/ebarchivesweb")
os.environ["DJANGO_SETTINGS_MODULE"] = "ebarchivesweb.settings"
django.setup()

from ebarchivesweb.models import *

path = "/home/tiago/Hacking/ebarchives/CSV"
os.chdir(path)

event_type = EventType.objects.get(type=type)
print("EVENT TYPE: " + str(event_type))
recurring = None
with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if row['RECURRING_TITLE_EN']:
            recurring = RecurringEvent.objects.get(title=row['RECURRING_TITLE_EN'])
        p = Event(title=row['TITLE_EN'],
                  title_fr=row['TITLE_FR'],
                  description=row['DESCRIPTION_EN'],
                  description_fr=row['DESCRIPTION_FR'],
                  recurring_event=recurring,
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
                    print("GETTING ARTIST: " + str.lower(a))
                    a = a.rstrip()
                    a_obj = Artist.objects.get(name=str.lower(a))
                    if a_obj:
                        p.artist.add(a_obj)
            p.save()

        # MEDIA MANYTOMANY
        if row['VIDEOS']:
            videos = row['VIDEOS'].split("\n")
            for v in videos:
                if v:
                    print("GETTING VIDEO: " + v)
                    v_obj = Media.objects.get(url=v)
                    if v_obj:
                        p.media.add(v_obj)
            p.save()

        if row['IMAGES/PDF']:
            videos = row['IMAGES/PDF'].split("\n")
            for v in videos:
                if v is not 'x' and v is not 'X' and v is not ' ' and v is not '':
                    print("GETTING IMAGES: " + v)
                    v_obj = Media.objects.get(url=v)
                    if v_obj:
                        p.media.add(v_obj)
            p.save()

        if row['AUDIO']:
            videos = row['AUDIO'].split("\n")
            for v in videos:
                if v is not 'x' and v is not 'X' and v is not ' ' and v is not '':
                    print("GETTING AUDIO: " + v)
                    v_obj = Media.objects.get(url=v)
                    if v_obj:
                        p.media.add(v_obj)
            p.save()
