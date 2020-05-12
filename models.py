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
	organizer=ForeignKeyField(User,backref='organized_events')
	attenders=ForeignKeyField(User,backref='attending_events')
	date=DateTimeField(default=datetime.datetime.now)
	comments=CharField() #should comments bbe its own model={user,event,time,text}
	description=CharField()
	street_address=TextField()
	city=TextField()
	state=TextField()
	zipcode=IntegerField()

	class Meta:
		database = DATABASE


class Chat(Model):
	sender=ForeignKeyField(User,backref='chats')
	recipient=ForeignKeyField(User,backref='chats')

	class Meta:
		database = DATABASE


class Message(Model):
	user_id=ForeignKeyField(User,backref="messages")
	message=TextField()
	post_time=DateTimeField(default=datetime.datetime.now)
	chat_id=ForeignKeyField(Chat,backref='messages')

	class Meta:
		database = DATABASE


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User,Event,Chat,Message], safe=True)
	print("Connected to the db and created tables, unless they already exist")
	DATABASE.close()
