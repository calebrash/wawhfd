import util
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    description = Column(String())
    image = Column(String())
    link = Column(String())
    deleted = Column(Boolean())

    def __init__(self, name, description=None, image=None, link=None, deleted=False):
        self.name = name
        self.description = description
        self.image = image
        self.link = link
        self.deleted = deleted

    def __repr__(self):
        return '<Recipe {name} ({id})>'.format(name=self.name, id=self.id)

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'name': self.name,
            'description': self.description,
            'image': self.image,
            'link': self.link,
        }

    @property
    def key(self):
        return util.get_key('recipe', self.id)

class CalenderEntry(Base):
    __tablename__ = 'calender_entries'

    id = Column(Integer, primary_key=True)
    date = Column(Date())
    recipe_id = Column(Integer, ForeignKey(Recipe.id))
    recipe = relationship('Recipe',
                          foreign_keys='CalenderEntry.recipe_id',
                          single_parent=True)

    def __init__(self, date, recipe_id=None, recipe=None):
        self.date = date
        self.recipe_id = recipe_id
        self.recipe = recipe

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'key': self.key,
            'date': self.date,
            'recipe_id': self.recipe_id,
            'recipe': self.recipe.as_dict,
        }

    @property
    def key(self):
        return util.get_key('cal-entry', self.id)

    @property
    def date_str(self):
        return self.date.strftime('%Y-%m-%d')
