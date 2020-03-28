from wedding_site import db

class RSVP(db.Model): 
    name = db.Column(db.String())
    email = db.Column(db.String(), primary_key=True)
    dietary_restrictions = db.Column(db.String())
    number_of_guests = db.Column(db.Integer())

    def __init__(self, name, email, number_of_guests, dietary_restrictions): 
      self.name = name 
      self.email = email
      self.dietary_restrictions = dietary_restrictions
      self.number_of_guests = number_of_guests

    def __repr__(self):
      return '<RSVP {}>'.format(self.body)


