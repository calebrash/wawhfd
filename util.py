def get_key_for_id(id):
    return 'recipe-{id}'.format(id=id)

def json_for_model(ModelClass):
    return [
        m.as_dict() for m in ModelClass.query.filter_by(deleted=False).order_by(ModelClass.id.asc())
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
