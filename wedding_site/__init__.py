from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
import os
from importlib import import_module

app = Flask(__name__, template_folder='static/templates')
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

for module_name in ['post', 'rsvp', 'user']:
    import_module(f'wedding_site.models.{module_name}', package=__name__)

from wedding_site.routes.routes import routes
app.register_blueprint(routes)
db.create_all()
