DATE_STRING_FORMAT = '%Y-%m-%d'

def get_key(name, id):
    return '{name}-{id}'.format(name=name, id=id)

def error_response(message):
    return JsonResponse({'error': message})

def model_list_response(Model, **kwargs):
    return JsonResponse({
        'data': [item.as_dict for item in Model.objects.filter(**kwargs)]
    })

COLLOQUIAL_DATE_LOOKUP = (
    'Today',
    'Tomorrow',
)

WEEKDAY_LOOKUP = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)
