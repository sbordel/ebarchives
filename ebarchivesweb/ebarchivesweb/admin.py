from django.contrib import admin
from .models import Event, EventType, RecurringEvent, Artist, Media
from suit.admin import SortableModelAdmin

class EventAdmin(SortableModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'year','type')
    sortable = 'order'
    autocomplete_fields = ['media', 'artist']

class ArtistAdmin(SortableModelAdmin):
    search_fields = ('name',)
    list_display = ('name', )
    sortable = 'order'

class MediaAdmin(admin.ModelAdmin):
    search_fields = ('url',)
    list_display = ('url', 'type')

class RecurringEventAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'title_fr', 'description', 'description_fr')

admin.site.register(EventType)
admin.site.register(RecurringEvent, RecurringEventAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Event, EventAdmin)
