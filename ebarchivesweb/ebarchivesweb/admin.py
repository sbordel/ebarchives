from django.contrib import admin
from .models import Event, EventType, RecurringEvent, Artist

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(RecurringEvent)
admin.site.register(Artist)