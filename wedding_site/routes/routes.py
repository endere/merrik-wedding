from flask import Blueprint, render_template, send_from_directory

routes = Blueprint('routes', __name__, template_folder='static/templates')

@routes.route('/')
def hello_world(): 
    print('cooooo?')
    return render_template('index.html')



@routes.route('/<path:path>')
def catch_all(path):
    return send_from_directory('static/templates', path)