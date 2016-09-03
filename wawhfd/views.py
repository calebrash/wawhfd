import datetime

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from wawhfd.models import Recipe, CalendarEntry
from wawhfd.constants import COLLOQUIAL_DATE_LOOKUP, WEEKDAY_LOOKUP, DATE_STRING_FORMAT

def error_response(message, status=500):
    return JsonResponse({
        'error': message,
    }, status=status)

def recipe_list_response():
    recipes = (
        Recipe.objects.filter(deleted=False)
        .extra(select={'iname': 'lower(name)'})
        .order_by('iname')
    )
    return JsonResponse({
        'data': [item.as_dict for item in recipes]
    })

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class DatesListView(View):
    def get(self, request):
        today = datetime.datetime.now()
        date_dicts = []
        date_map = {}
        dates = []

        for d in range(0, settings.WAWHFD_NUM_DATES):
            date = today + datetime.timedelta(days=d)
            if d in (0, 1,):
                date_name = COLLOQUIAL_DATE_LOOKUP[d]
            else:
                date_name = WEEKDAY_LOOKUP[date.weekday()]
            date_formatted = date.strftime(DATE_STRING_FORMAT)
            dates.append(date_formatted)
            date_map[date_formatted] = d
            date_dicts.append({
                'key': 'date-{d}'.format(d=date_formatted),
                'date': date_formatted,
                'date_string': date.strftime('%B %d, %Y'),
                'title': date_name,
                'description': 'Description for item {index}'.format(index=d)
            })

        entries = CalendarEntry.objects.filter(date__in=dates)
        for entry in entries:
            date_dicts[date_map[entry.date_str]]['recipe'] = entry.recipe.as_dict

        return JsonResponse({
            'data': date_dicts
        })

class DatesEditView(View):
    def post(self, request, date_str):
        date_obj = datetime.datetime.strptime(date_str, DATE_STRING_FORMAT)
        try:
            entry = CalendarEntry.objects.get(date=date_obj)
        except CalendarEntry.DoesNotExist:
            entry = CalendarEntry(date=date_obj)
        
        entry.recipe_id = request.POST.get('id')
        entry.save()
        return JsonResponse(entry.as_dict)

class DatesDeleteView(View):
    def post(self, request, date_str):
        try:
            entry = CalendarEntry.objects.get(date=date_str)
        except CalendarEntry.DoesNotExist:
            return error_response('Date {date} does not exist'.format(date=date_str), status=404)
        entry.delete()
        return JsonResponse({
            'success': True
        })

class RecipesListView(View):
    def get(self, request):
        return recipe_list_response()

class RecipesAddView(View):
    def post(self, request):
        try:
            recipe = Recipe(name=request.POST.get('name'),
                            description=request.POST.get('description'),
                            link=request.POST.get('link'))
            recipe.save()
        except:
            return error_response('Could not create recipe')
        return recipe_list_response()

class RecipesEditView(View):
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return error_response('Recipe {id} does not exist'.format(id=recipe_id), status=404)

        recipe.name = request.POST.get('name')
        recipe.description = request.POST.get('description')
        recipe.link = request.POST.get('link')

        try:
            recipe.save()
        except:
            return error_response('Could not update recipe {id}'.format(id=recipe_id))

        return recipe_list_response()

class RecipesDeleteView(View):
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return error_response('Recipe {id} does not exist'.format(id=recipe_id), status=404)
        recipe.deleted = True
        recipe.save()
        CalendarEntry.objects.filter(recipe_id=recipe_id).delete()
        return recipe_list_response()
