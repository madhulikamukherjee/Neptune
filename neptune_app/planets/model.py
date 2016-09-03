from mongoengine.fields import (URLField, DictField, BooleanField, StringField,
	ListField, DateTimeField, FloatField)
from neptune_app import db, app

class Planets(db.Document):
	planet_id = db.StringField()
	name = db.StringField()
	radius = db.FloatField()
	mass_wrt_earth = db.FloatField()
	moons = db.ListField()

	@property
	def repr(self):
		return {
			'id':	   self.planet_id,
			'name':	 self.name,
			'radius':   self.radius,
			'mass_wrt_earth': self.mass_wrt_earth,
			'moons': self.moons
		}