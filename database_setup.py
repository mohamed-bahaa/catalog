import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

"""User class """


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

"""Category class """


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return object data in serializeable format
        return {
            'id': self.id,
            'name': self.name,
        }
"""Book class """


class Book(Base):
    __tablename__ = 'book'

    name = Column(String(80), nullable=False)
    description = Column(String(250))
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Return object data in serializeable format"""
        return {
            'category': self.category.name,
            'description': self.description,
            'name': self.name,
        }

engine = create_engine('sqlite:///books_catalog.db', connect_args={'check_same_thread':False})
Base.metadata.create_all(engine)
