import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user



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

@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	# payload['username'] = payload['username'].lower()
	print("payload",payload)

	try: 
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)

		checked_password = check_password_hash(user_dict['password'],payload['password'])
		if(checked_password):
			login_user(user)
			print(f"{current_user.username} is current_user.username->POST @ /users/login")
			user_dict.pop('password')
			print("current_user table id num is",current_user)
			return jsonify(
				data=user_dict,
				message=f"logged in as {user_dict['email']}",
				status=200,

				),200
		else:
			print('incorrect password')
			return jsonify(
				data={},
				message="email or password is incorrect",
				status=401
				),401

	except models.DoesNotExist:
		print("incorrect  username")
		return jsonify(
			data={},
			message="email or password is incorrect",
			status=401
			),401

@users.route('/logout', methods=["GET"])
def logout():
	logout_user()
	print('current_user',current_user)
	return jsonify(
		data={},
		message="Successfully logged out user",
		status=200
		),200






















