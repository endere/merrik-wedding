from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import os
from wedding_site import routes, models

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
