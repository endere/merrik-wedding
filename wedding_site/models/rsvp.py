from wedding_site import db
from .user import user

class RSVP(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  num_reported = db.Column(db.Integer())
  response = db.Column(db.Boolean(), index=True)
  resp_num = db.Column(db.Integer())
  resp_exp = db.Column(db.Integer())

  def __repr__(self):
    return '<RSVP {}>'.format(self.body)


