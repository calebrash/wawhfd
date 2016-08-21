import datetime
import json
import util
from flask import Flask, render_template, jsonify

app = Flask(__name__)

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
            'content': 'Content for item {index}'.format(index=d)
        })
    return jsonify(dates)

RECIPES = [{
    'id': 1,
    'name': 'Test recipe',
    'content': 'This recipe is awesome',
    'image': None,
    'link': None,
},{
    'id': 2,
    'name': 'Another recipe',
    'content': None,
    'image': None,
    'link': 'https://google.com',
}]

@app.route('/api/recipes/', methods=['GET'])
def api_recipes_list():
    for recipe in RECIPES:
        recipe['key'] = 'recipe-{id}'.format(id=recipe['id'])
    return jsonify(RECIPES)

@app.route('/api/recipes/add/', methods=['POST'])
def api_recipes_add():
    recipe = request.form
    recipe['id'] = len(RECIPES) + 1
    return jsonify(recipe)

@app.route('/api/recipes/<int:recipe_id>/edit/', methods=['POST'])
def api_recipes_edit(recipe_id):
    result = None
    for recipe in RECIPES:
        if recipe['id'] == recipe_id:
            result = recipe
            break
    if result:
        result['name'] = request.form['name']
        result['success'] = True
    else:
        result = {
            'success': False
        }
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
