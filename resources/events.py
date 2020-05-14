import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required
import datetime
from datetime import date

events = Blueprint('events','events')

@events.route('/',methods=['GET'])
def all_events():
	all_event_dicts = [model_to_dict(event) for event in models.Event.select()]
	print(all_event_dicts)
	return jsonify({
		'data':all_event_dicts,
		'message':"hello"
		})
	

@events.route('/add',methods=['POST'])
@login_required
def create_event():

	payload = request.get_json()

	years = (payload['years'])
	months = (payload['months']) 
	days = (payload['days']) 
	hours = (payload['hours']) # remember to change 12 hours to 24 in react req
	mins = (payload['minutes'] )
	secs = 0
	date_time = datetime.datetime(
		int(years),
		int(months),
		int(days),
		int(hours),
		int(mins),
		int(secs)
		)	
	time = date_time.strftime('%I:%M:%p')
	print("current_user",current_user) 
	

	new_event = models.Event.create(
		name=payload['name'],
		organizer=current_user.id,
		date_time=time,
		street_address=payload['street_address'],
		city=payload['city'],
		state=payload['state'],
		zipcode=payload['zipcode'],
		description=payload['description'],
		picture=payload['picture'],
		)
	print(new_event)
	print(new_event.__dict__)

	event_dict=model_to_dict(new_event)

	return jsonify(
		# data=event_dict,
		message='success you added a new event',
		status=201
		),201





















