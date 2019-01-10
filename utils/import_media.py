#!/usr/bin/python3
# -*- coding: utf-

import os, csv, sys, django, string

sys.path.append("/home/tiago/Hacking/ebarchives/ebarchivesweb")
os.environ["DJANGO_SETTINGS_MODULE"] = "ebarchivesweb.settings"
django.setup()

from ebarchivesweb.models import *

path = "/home/tiago/Hacking/ebarchives/CSV"
os.chdir(path)

with open('media.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['IMAGES/PDF'] is not '' and row['IMAGES/PDF'] is not 'x' and row['IMAGES/PDF'] is not 'X':
            i = Media(url=row['IMAGES/PDF'], type='image')
            print(i)
            i.save()
        if row['AUDIO'] is not '' and row['AUDIO'] is not 'x' and row['AUDIO'] is not 'X':
            a_list = row['AUDIO'].split('\n')
            for i in a_list:
                a = Media(url=i, type='audio')
                print(a)
                a.save()
        if row['VIDEOS'] is not '' and row['VIDEOS'] is not 'x' and row['VIDEOS'] is not 'X' :
            v_list = row['VIDEOS'].split('\n')
            for i in v_list:
                v = Media(url=i, type='video')
                print(v)
                v.save()
