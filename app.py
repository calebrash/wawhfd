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

from database import init_db, db_session
from models import Recipe
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
init_db()



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
    return jsonify(util.json_for_model(Recipe))

@app.route('/api/recipes/add/', methods=['POST'])
def api_recipes_add():
    recipe = Recipe(name=request.form.get('name'),
                    description=request.form.get('description'),
                    link=request.form.get('link'))
    db_session.add(recipe)
    db_session.commit()
    return jsonify(util.json_for_model(Recipe))

@app.route('/api/recipes/<int:recipe_id>/edit/', methods=['POST'])
def api_recipes_edit(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    recipe.name = request.form.get('name')
    recipe.description = request.form.get('description')
    recipe.image = None
    recipe.link = request.form.get('link')
    db_session.add(recipe)
    db_session.commit()
    return jsonify(util.json_for_model(Recipe))

@app.route('/api/recipes/<int:recipe_id>/delete/', methods=['POST'])
def api_recipes_delete(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    recipe.deleted = True
    db_session.add(recipe)
    db_session.commit()
    return jsonify(util.json_for_model(Recipe))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
