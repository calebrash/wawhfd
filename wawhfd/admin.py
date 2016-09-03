from django.contrib import admin

from wawhfd.models import Recipe, CalendarEntry

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'link', 'deleted',)

class CalendarEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'recipe_str',)

    def recipe_str(self, entry):
        return 'Recipe: {name} ({id})'.format(name=entry.recipe.name, id=entry.recipe.id)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(CalendarEntry, CalendarEntryAdmin)
