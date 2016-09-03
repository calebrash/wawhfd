from django.contrib import admin

from wawhfd.models import Recipe, CalendarEntry

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'link', 'deleted',)

class CalendarEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'link', 'deleted',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(CalendarEntry)
