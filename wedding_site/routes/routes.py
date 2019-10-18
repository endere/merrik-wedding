from flask import Blueprint, render_template

routes = Blueprint('routes', __name__, template_folder='static/templates')

@routes.route('/')
def hello_world(): 
  return render_template('base.html', message='Hello Wedding!')
