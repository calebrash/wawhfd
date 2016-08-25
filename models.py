from app import db
from sqlalchemy.dialects.postgresql import JSON

import util


class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    image = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self, name, description=None, image=None, link=None):
        self.name = name
        self.description = description
        self.image = image
        self.link = link

    def key(self):
        return util.get_key_for_id(self.id),
