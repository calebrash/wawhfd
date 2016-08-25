import datetime
import json
import util
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/calejandro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Recipe



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dates/', methods=['GET'])
def api_dates_list():
    today = datetime.datetime.now()
    dates = []
    for d in range(0, 9):
        date = today + datetime.timedelta(days=d)
        if d in (0, 1,):
            date_name = util.colloquial_date_lookup[d]
        else:
            date_name = util.weekday_lookup[date.weekday()]
        dates.append({
            'key': 'date-item-{index}'.format(index=d),
            'date': date,
            'date_string': date.strftime('%B %d, %Y'),
            'title': date_name,
            'description': 'Description for item {index}'.format(index=d)
        })
    return jsonify(dates)

@app.route('/api/recipes/', methods=['GET'])
def api_recipes_list():
    return jsonify(util.RECIPES)

@app.route('/api/recipes/add/', methods=['POST'])
def api_recipes_add():
    recipe = {
        'id': len(util.RECIPES) + 1,
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'image': None,
        'link': request.form.get('link'),
    }
    recipe['key'] = util.get_key_for_id(recipe['id'])
    util.RECIPES.insert(0, recipe)
    return jsonify(util.RECIPES)

@app.route('/api/recipes/<int:recipe_id>/edit/', methods=['POST'])
def api_recipes_edit(recipe_id):
    recipe = {
        'id': recipe_id,
        'key': util.get_key_for_id(recipe_id),
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'image': None,
        'link': request.form.get('link'),
    }
    for index, r in enumerate(util.RECIPES):
        print('   [r] %s' % index)
        if r['id'] == recipe['id']:
            util.RECIPES[index] = recipe
            break
    return jsonify(util.RECIPES)


if __name__ == '__main__':
    app.run(debug=True)
