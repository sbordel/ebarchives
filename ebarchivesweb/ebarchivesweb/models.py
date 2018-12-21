from django.db import models

EVENT_CHOICES = (
    (
        "conference",
        "Conference / Panel",
    ),
    (
        "event",
        "Event",
    ),
    (
        "festival",
        "Festival",
    ),
    (
        "misc",
        "Misc",
    ),
    (
        "radio",
        "Radio",
    ),
    (
        "residence",
        "Residence",
    ),
    (
        "workshop",
        "Workshop",
    ),
    (
        "exhibit",
        "Exhibit",
    )
)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

class EventType(models.Model):
    type = models.CharField(choices=EVENT_CHOICES, max_length=200)
    recurring_event = models.ForeignKey('RecurringEvent', on_delete=models.SET_NULL, null=True)

class RecurringEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
