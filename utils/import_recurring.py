#!/usr/bin/python3
# -*- coding: utf-

import os, csv, sys, django, string

sys.path.append("/home/tiago/Hacking/ebarchives/ebarchivesweb")
os.environ["DJANGO_SETTINGS_MODULE"] = "ebarchivesweb.settings"
django.setup()

from ebarchivesweb.models import *

path = "/home/tiago/Hacking/ebarchives/CSV"
os.chdir(path)

with open('recurring.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['RECURRING_TITLE_EN'] is not '':
            p = RecurringEvent(title=row['RECURRING_TITLE_EN'], title_fr=row['RECURRING_TITLE_FR'], description=row['RECURRING_DESCRIPTION_EN'], description_fr=row['RECURRING_DESCRIPTION_FR'])
            print(p)
            p.save()
