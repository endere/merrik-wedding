from datetime import datetime
from wedding_site import db 
from .user import User

class Post(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.Forignkey('user.id'))
  body = db.Column(db.String(288))
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __repr__(self): 
    return '<Post {}>'.format(self.body)

