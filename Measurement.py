import webapp2
import logging
from google.appengine.ext import ndb


class Measurement(ndb.Model):
	"""Models an individual measurement."""
	conductivity = ndb.StringProperty()
	brightness = ndb.StringProperty()
	temperature = ndb.StringProperty()
	date = ndb.DateTimeProperty(auto_now_add=True)
