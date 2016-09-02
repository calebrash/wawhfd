DATE_STRING_FORMAT = '%Y-%m-%d'

def get_key(name, id):
    return '{name}-{id}'.format(name=name, id=id)

def json_for_model(ModelClass):
    return [
        m.as_dict for m in ModelClass.query.filter_by(deleted=False).order_by(ModelClass.id.asc())
    ]

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
