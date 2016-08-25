def get_key_for_id(id):
    return 'recipe-{id}'.format(id=id)

RECIPES = [{
    'id': 1,
    'key': get_key_for_id(1),
    'name': 'Test recipe',
    'description': 'This recipe is awesome',
    'image': None,
    'link': None,
},{
    'id': 2,
    'key': get_key_for_id(2),
    'name': 'Another recipe',
    'description': None,
    'image': None,
    'link': 'https://google.com',
},{
    'id': 3,
    'key': get_key_for_id(3),
    'name': 'Monkey stew',
    'description': 'Akldjfalsjdflsdaf',
    'image': None,
    'link': 'https://google.com',
}]

colloquial_date_lookup = (
    'Today',
    'Tomorrow',
)

weekday_lookup = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)
