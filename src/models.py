import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'),primary_key=True, nullable= False)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable= False)

class User(Base):
    __tablename__ = 'user'
    # Aquí definimos columnas para la persona de la mesa.
    # Observe que cada columna también es un atributo de instancia normal de Python.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    firtname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
  

class Comment(Base):
    __tablename__ = 'comment'
    # Aquí definimos columnas para la dirección de la tabla.
    # Observe que cada columna también es un atributo de instancia normal de Python.
    id = Column(Integer, primary_key=True)
    comentario_text = Column(String(250), nullable=False)
    autor_id = Column (Integer, ForeignKey("user.id"))
    post_id = Column (Integer, ForeignKey("post.id"))

class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    user_id = Column(String(250),ForeignKey("user.id"), nullable=False)

class Media (Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(String(250), ForeignKey("post.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
