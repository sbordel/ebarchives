from django.db import models

EVENT_CHOICES = (
    (
        "talk",
        "Talk/Conference/Panel",
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
    title_fr = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)
    artist = models.ManyToManyField('Artist', blank=True)
    media = models.ManyToManyField('Media', blank=True)
    type = models.ForeignKey('EventType', on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    comment = models.TextField(null=True, blank=True)
    recurring_event = models.ForeignKey('RecurringEvent', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(null=True, blank=True)

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
    name = models.CharField(max_length=200)
    order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

class EventType(models.Model):
    type = models.CharField(choices=EVENT_CHOICES, max_length=200)

    def __str__(self):
        return "%s" % (self.type)

class RecurringEvent(models.Model):
    title = models.CharField(max_length=200)
    title_fr = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description_fr = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.title)
