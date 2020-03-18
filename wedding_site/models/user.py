from wedding_site import db 

class User(db.Model): 
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(128), index=True, unique=True)
  email = db.Column(db.String(128), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  def __init__(self, username, email, password_hash): 
    self.username = username 
    self.email = email 
    self.password_hash = password_hash
    
  def __repr__(self): 
    return '<User {}>'.format(self.username)
