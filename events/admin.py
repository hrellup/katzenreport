from __future__ import unicode_literals

from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
       return False

    date_hierarchy = 'datum'
    list_filter = ('computer','mensch')
    list_editable = ('mensch',)
    list_link = ('admin_image',)
    list_display = ('datum', 'eingangswert', 'ausgangswert', 'computer','bild',  'mensch', 'cmp_check')


admin.site.register(Event, EventAdmin)
