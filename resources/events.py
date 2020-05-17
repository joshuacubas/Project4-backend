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
		'message':"hello",
		'status':200,
		}),200

@events.route('/manage/myevents')
@login_required
def my_organized_events():

	my_events = [model_to_dict(event) for event in models.Event.select().where(models.Event.organizer == current_user.id)]
 
	print("my_events",my_events)

	return jsonify(
		data=my_events,
		message= f"found {len(my_events)} events organized by logged in user ",
		status=200
		),200

@events.route('/add',methods=['POST'])
@login_required
def create_event():

	payload = request.get_json()

	years = (payload['years'])
	months = (payload['months']) 
	days = (payload['days']) 
	hours = (payload['hours']) # remember to change 12 hours to 24 in react req
	mins = (payload['minutes'] )
	date_time = datetime.datetime(
		int(years),
		int(months),
		int(days),
		int(hours),
		int(mins)
		)	
	time = date_time.strftime('%I:%M:%p')
	day = date_time.strftime('%A, %B %d, %Y')
	print("day",day)
	print("current_user",current_user) 
	

	new_event = models.Event.create(
		name=payload['name'],
		organizer=current_user.id,
		date_time=time,
		date_day=day,
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



@events.route('/manage/<id>',methods=['DELETE'])
@login_required
def delete_event(id):
	#make sure only this user can delete their own
	delete_query= models.Event.delete().where(models.Event.id == id)
	num_of_rows_deleted = delete_query.execute()
	print("num_of_rows_deleted --->-->-->",num_of_rows_deleted)
	return jsonify(
		data={},
		message = f"Successfully deleted {num_of_rows_deleted} event(s), with id: {id}.",
		status=200
		),200

@events.route('/manage/<id>',methods=['PUT'])
@login_required
def update_event(id):
	payload = request.get_json()


	years = (payload['years'])
	months = (payload['months']) 
	days = (payload['days']) 
	hours = (payload['hours']) # remember to change 12 hours to 24 in react req
	mins = (payload['minutes'] )
	date_time = datetime.datetime(
		int(years),
		int(months),
		int(days),
		int(hours),
		int(mins)
		)	
	time = date_time.strftime('%I:%M:%p')
	day = date_time.strftime('%A, %B %d, %Y')

	update_query = models.Event.update(
		name=payload['name'],
		date_time=time,
		date_day=day,
		street_address=payload['street_address'],
		city=payload['city'],
		state=payload['state'],
		zipcode=payload['zipcode'],
		description=payload['description'],
		picture=payload['picture'],
		).where(models.Event.id == id)
	num_of_rows_changed = update_query.execute()
	updated_event = models.Event.get_by_id(id)
	updated_event_dict = model_to_dict(updated_event)

	return jsonify(
		data={},
		message=f"Successfully update recipe, with id of {id}",
		status=200
		),200
















