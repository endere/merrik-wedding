from wedding_site import db

class RSVP(db.Model): 
    name = db.Column(db.String())
    email = db.Column(db.String(), primary_key=True)
    number_of_guests = db.Column(db.Integer())
    meal_preference = db.Column(db.String())

    def __init__(self, name, email, number_of_guests, meal_preference): 
      self.name = name 
      self.email = email
      self.number_of_guests = number_of_guests
      self.meal_preference = meal_preference

    def __repr__(self):
      return '<RSVP {}>'.format(self.body)


