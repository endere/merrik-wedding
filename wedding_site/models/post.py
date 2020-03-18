from datetime import datetime
from wedding_site import db 

class Post(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  body = db.Column(db.String(288))
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __init__(self, user_id, body, timestamp):
     self.user_id = user_id 
     self.body = body
     self.timestamp = timestamp

  def __repr__(self): 
    return '<Post {}>'.format(self.body)

