from flask import Flask, jsonify
import models
from resources.users import users
from resources.events import events
from flask_login import LoginManager, current_user
from flask_cors import CORS

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key="ScoobyDoobyDooWhereArtThou"



login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	try:
		return models.User.get_by_id(user_id)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data = {'error':'User is not logged in'},
		message = "Must be logged in to access",
		status = 401 
		),401


CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(events, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(events, url_prefix='/api/v1/events')



@app.route('/')
def hello():
	return 'Hello, World. Testing ... 1 ... 2 ... 3'
	print('sdjfhskdj')


































if __name__=='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)