from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    #recipes = db.relationship('Recipe')



class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #date_created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    #image_url = db.Column(db.String(100), nullable=True)
    #rating = db.Column(db.Float, default=0.0)
    #num_ratings = db.Column(db.Integer, default=0)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #comments = db.relationship('Comment', backref='recipe', lazy=True)

    #create a function to return a string when we add something.
    def __repr__(self):
        return '<name %r>' % self.id
   
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    #recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

 

