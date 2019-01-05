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

MEDIA_CHOICES = (
    (
        "image",
        "Image",
    ),
    (
        "audio",
        "Audio",
    ),
    (
        "video",
        "Video",
    ),
    (
        "other",
        "Other",
    )
)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    media = models.ManyToManyField('Media', blank=True)
    type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return "%s" % (self.title)

class Media(models.Model):
    type = models.CharField(choices=MEDIA_CHOICES, max_length=200)
    # for audio, video and other: URL
    # for image: local folder path
    url = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.url)

class Artist(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class EventType(models.Model):
    type = models.CharField(choices=EVENT_CHOICES, max_length=200)
    recurring_event = models.ForeignKey('RecurringEvent', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.type)

class RecurringEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.title)
