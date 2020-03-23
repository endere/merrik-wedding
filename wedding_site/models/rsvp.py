from wedding_site import db

class RSVP(db.Model): 
    name = db.Column(db.String())
    email = db.Column(db.String(), primary_key=True)
    meal_preference = db.Column(db.String())

    def __init__(self, name, email, meal_preference): 
      self.name = name 
      self.email = email
      self.meal_preference = meal_preference

    def __repr__(self):
      return '<RSVP {}>'.format(self.body)


