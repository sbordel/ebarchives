#!/usr/bin/python3
# -*- coding: utf-

import os, csv, sys, django, string

sys.path.append("/home/tvaz/Hacking/ebarchives/ebarchivesweb")
os.environ["DJANGO_SETTINGS_MODULE"] = "ebarchivesweb.settings"
django.setup()

from ebarchivesweb.models import *

path = "/home/tvaz/Hacking/ebarchives/CSV"
os.chdir(path)

with open('artists') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Artist(name=row['artist'])
        print(p)
        p.save()
