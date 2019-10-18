from flask import Flask
from wedding_site.routes.routes import routes

app = Flask(__name__, template_folder='static/templates')
print('hello world!!!')


app.register_blueprint(routes)

if __name__ == '__main__': 
  app.run(host='0.0.0.0', debug=True)  