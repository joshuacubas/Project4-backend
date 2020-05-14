from peewee import *
from flask_login import UserMixin
import datetime

DATABASE = SqliteDatabase('events.sqlite')


class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()
	city=TextField()
	state=TextField()
	picture=TextField()

	class Meta:
		database = DATABASE



class Event(Model):
	name=CharField()
	organizer=ForeignKeyField(User,backref='organized_events')
	date_time=TextField()
	description=CharField()
	street_address=TextField()
	city=TextField()
	state=TextField()
	zipcode=TextField()
	picture=TextField()
	# date_month=payload['date_month'],
	# date_day=payload['date_day'],
	# date_year=payload['date_year'],
	# time_hr=payload['time_hr'],
	# time_min=payload['time_min'],
	# time_ampm=payload['time_ampm'],

	class Meta:
		database = DATABASE

class Comment(Model):
	event=ForeignKeyField(Event,backref='comments')
	author=ForeignKeyField(User,backref='comments')
	description=TextField()
	posted_time=DateTimeField(default=datetime.datetime.now)

	class Meta:
		datetime=DATABASE


class Chat(Model):
	sender=ForeignKeyField(User,backref='chats')
	recipient=ForeignKeyField(User,backref='chats')

	class Meta:
		database = DATABASE


class Message(Model):
	user_id=ForeignKeyField(User,backref="messages")
	message=TextField()
	posted_time=DateTimeField(default=datetime.datetime.now)
	chat_id=ForeignKeyField(Chat,backref='messages')

	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User,Event,Chat,Message], safe=True)
	print("Connected to the db and created tables, unless they already exist")
	DATABASE.close()
