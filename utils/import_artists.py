#!/usr/bin/python3
# -*- coding: utf-

import os, csv, sys, django, string

sys.path.append("/home/tiago/Hacking/ebarchives/ebarchivesweb")
os.environ["DJANGO_SETTINGS_MODULE"] = "ebarchivesweb.settings"
django.setup()

from ebarchivesweb.models import *

path = "/home/tiago/Hacking/ebarchives/CSV"
os.chdir(path)

with open('artists.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Artist(name=row['artist'].rstrip())
        print(p)
        p.save()
