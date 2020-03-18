from flask import Blueprint, render_template, send_from_directory

routes = Blueprint('routes', __name__, template_folder='static/templates')

@routes.route('/')
def hello_world(): 
    return render_template('index.html')


@routes.route('/venue')
def venue(): 
    return render_template('venue.html')


@routes.route('/accomodation')
def accomodation(): 
    return render_template('accomodation.html')





@routes.route('/<path:path>')
def catch_all(path):
    return send_from_directory('static/templates', path)
          