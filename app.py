from flask import Flask, jsonify
import models
from resources.users import users
from flask_login import LoginManager


DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key="ScoobyDoobyDooWhereArtThou"

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(users, url_prefix='/api/v1/users')



@app.route('/')
def hello():
	return 'Hello, World. Testing ... 1 ... 2 ... 3'
	print('sdjfhskdj')


































if __name__=='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)