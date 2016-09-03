from mongoengine.fields import (URLField, DictField, BooleanField, StringField,
	ListField, DateTimeField, FloatField)
from neptune_app import db, app

class Moons(db.Document):
	moon_id = db.StringField()
	name = db.StringField()
	discovery_date = db.StringField()
	discoverer = db.StringField()

	@property
	def repr(self):
		return {
			'moon_id':	   self.moon_id,
			'name':	 self.name,
			'discovery_date':   self.discovery_date,
			'discoverer': self.discoverer
		}