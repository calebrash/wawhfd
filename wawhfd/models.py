from django.db import models
from wawhfd.constants import DATE_STRING_FORMAT


def get_key(name, id):
    return '{name}-{id}'.format(name=name, id=id)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    deleted = models.BooleanField(default=False)

    @property
    def key(self):
        return get_key('recipe', self.id)

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'link': self.link,
            'key': self.key,
        }

class CalendarEntry(models.Model):
    date = models.DateField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    @property
    def key(self):
        return get_key('cal-entry', self.id)

    @property
    def date_str(self):
        return self.date.strftime(DATE_STRING_FORMAT)

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'recipe': self.recipe.as_dict,
            'key': self.key,
            'date_str': self.date_str,
        }
