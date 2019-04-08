#from app import db,bcrypt, app
from app import db
import datetime
#from flask_security import Security



class Pic(db.Model):
	identifier = db.Column(db.Integer, primary_key=True, autoincrement=True)
	#encoding = db.Column(db.Float, primary_key=True)
	encoding = db.Column(db.ARRAY(sa.Integer()))
	description = db.Column(db.String(2048))
	
	
	

	def __init__(self, description,encoding):
		self.encoding = encoding
		self.description = description
		

	def __repr__(self):
		return '<Pic %r>' % (self.description)
		

