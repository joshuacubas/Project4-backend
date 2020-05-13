import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user



users = Blueprint('users','users')

@users.route('/', methods=['GET'])
def sample_test_route():
	return "user sample_test_route called and working"

@users.route('/register', methods=['POST'])
def register():
	payload=request.get_json()
	print("payload",payload)

	payload['email']=payload['email'].lower()
	payload['username']=payload['username'].lower()
	print("payload after l/c",payload)

	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(
			data={},
			message="A user registered with this email already exists.",
			status=401
			),401
	except models.DoesNotExist:

		try:
			models.User.get(models.User.username == payload['username'])
			return jsonify(
				data={},
				message="A user with this username already exists.",
				status=401
				),401
		except models.DoesNotExist:
			pw_hash = generate_password_hash(payload['password'])
			created_user = models.User.create(
				username = payload['username'],
				email = payload['email'],
				password = pw_hash,
				city = payload['city'],
				state = payload['state'],
				picture = payload['picture']
				)
			login_user(created_user)
			created_user_dict = model_to_dict(created_user)
			print(created_user_dict)
			created_user_dict.pop('password')

			return jsonify(
				data=created_user_dict,
				message="registered a new user",
				status=201
				),201























