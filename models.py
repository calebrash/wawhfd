import util
from sqlalchemy import Column, Integer, String, Boolean
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
        return util.get_key_for_id(self.id)
