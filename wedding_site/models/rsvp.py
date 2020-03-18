from wedding_site import db

class RSVP(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  num_reported = db.Column(db.Integer())
  response = db.Column(db.Boolean(), index=True)
  resp_num = db.Column(db.Integer())
  resp_exp = db.Column(db.Integer())

  def __init__(self, user_id, num_reported, response, resp_num, resp_exp): 
    self.user_id = user_id
    self.num_reported = num_reported 
    self.response = response
    self.resp_num = resp_num
    self.resp_exp = resp_exp

  def __repr__(self):
    return '<RSVP {}>'.format(self.body)


