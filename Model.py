from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Comment(db.Model):
    __tablename__ = 'comments'


class Category(db.Model):
    __tablename__ = 'categories'


class CategorySchema(ma.Schema):

class CommentSchema(ma.Schema):
