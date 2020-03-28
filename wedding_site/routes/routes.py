from flask import Blueprint, render_template, send_from_directory, request
from wedding_site.models.rsvp import RSVP, db
routes = Blueprint('routes', __name__, template_folder='static/templates')

@routes.route('/')
def hello_world(): 
    return render_template('index.html')

@routes.route('/venue')
def venue(): 
    return render_template('venue.html')

@routes.route('/accommodation')
def accommodation(): 
    return render_template('accommodation.html')

@routes.route('/rsvp')
def rsvp(): 
    return render_template('rsvp.html')

@routes.route('/confirm-rsvp', methods=["POST"])
def confirm_rsvp(): 
    rsvp = RSVP.query.filter_by(email=request.values['email']).first()
    if rsvp:
        rsvp.name = request.values['name']
        rsvp.dietary_restrictions = request.values['dietary_restrictions']
        rsvp.number_of_guests = request.values['number_of_guests']
    else:
        rsvp = RSVP(name=request.values['name'], email=request.values['email'], dietary_restrictions=request.values['dietary_restrictions'], number_of_guests=request.values['number_of_guests'])
        db.session.add(rsvp)
    db.session.commit()
    return render_template('generic.html', title='RSVP successful', message='Your RSVP has been submitted! Thank you!')

@routes.route('/<path:path>')
def catch_all(path):
    """Catch all for the base template path. All other template fragments are built on this."""
    return send_from_directory('static/templates', path)
          