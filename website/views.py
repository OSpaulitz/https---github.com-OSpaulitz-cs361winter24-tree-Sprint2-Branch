from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Recipe  # add recipe and comment like note example line #14
from . import db
import json

views = Blueprint('views', __name__)

### i should put all non authorizated user pages

#@views.route('/sample')
#def sample():
#    return render_template("sample.html")

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


#creating a page where a user can view specific recipes.  make sure this is aligned with database models and recipe.html*** remember to revert back to: recipe_name = request.form['name']
@views.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == "POST":
        recipe_name = request.form['name']
        recipe_category = request.form['category']
        recipe_ingredients = request.form['ingredients']
        recipe_instructions = request.form['instructions']
        new_recipe = Recipe(name=recipe_name, category=recipe_category, ingredients=recipe_ingredients, instructions=recipe_instructions)#, user_id=current_user.id)

        #push to database
        try:
            db.session.add(new_recipe)
            db.session.commit()
            return redirect('/recipe')
        except Exception as e:
            db.session.rollback()
            print(f"Error adding recipe:{str(e)}")
            return "There was an error adding your recipe"

    else:
        recipe = Recipe.query.order_by(Recipe.name.desc())
        return render_template("recipe.html", user=current_user, recipe=recipe)
    
    #i think it needs Recipe bc that's what i called the class in models.py

