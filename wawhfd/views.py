import datetime

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from wawhfd.models import Recipe, CalenderEntry
from wawhfd.util import colloquial_date_lookup, weekday_lookup, DATE_STRING_FORMAT


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
                date_name = colloquial_date_lookup[d]
            else:
                date_name = weekday_lookup[date.weekday()]
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

        entries = CalenderEntry.objects.filter(date__in=dates)
        for entry in entries:
            date_dicts[date_map[entry.date_str]]['recipe'] = entry.recipe.as_dict

        return JsonResponse({
            'data': date_dicts
        })

class DatesEditView(View):
    def post(self, request, date_str):
        date_obj = datetime.datetime.strptime(date_str, DATE_STRING_FORMAT)
        try:
            entry = CalenderEntry.objects.get(date=date_obj)
        except CalenderEntry.DoesNotExist:
            entry = CalenderEntry(date=date_obj)
        
        entry.recipe_id = request.POST.get('id')
        entry.save()
        return JsonResponse(entry.as_dict)

class DatesDeleteView(View):
    def post(self, request, date_str):
        try:
            entry = CalenderEntry.objects.get(date=date_str)
        except CalenderEntry.DoesNotExist:
            return error_response('Date {date} does not exist'.format(date=date_str))
        entry.delete()
        return JsonResponse({
            'success': True
        })

def error_response(message):
    return JsonResponse({'error': message})

def model_list_response(Model, **kwargs):
    return JsonResponse({
        'data': [item.as_dict for item in Model.objects.filter(**kwargs)]
    })

class RecipesListView(View):
    def get(self, request):
        return model_list_response(Recipe, deleted=False)

class RecipesAddView(View):
    def post(self, request):
        try:
            recipe = Recipe(name=request.POST.get('name'),
                            description=request.POST.get('description'),
                            link=request.POST.get('link'))
            recipe.save()
        except:
            return error_response('Could not create recipe')
        return model_list_response(Recipe, deleted=False)

class RecipesEditView(View):
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return error_response('Recipe {id} does not exist'.format(id=recipe_id))

        recipe.name = request.POST.get('name')
        recipe.description = request.POST.get('description')
        recipe.link = request.POST.get('link')

        try:
            recipe.save()
        except:
            return error_response('Could not update recipe {id}'.format(id=recipe_id))

        return model_list_response(Recipe, deleted=False)

class RecipesDeleteView(View):
    def post(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return error_response('Recipe {id} does not exist'.format(id=recipe_id))
        recipe.deleted = True
        recipe.save()
        CalenderEntry.objects.filter(recipe_id=recipe_id).delete()
        return model_list_response(Recipe, deleted=False)
