import webapp2
import os
import logging
from Converter import Converter
from Measurement import Measurement
from google.appengine.ext import ndb
from google.appengine.ext.db import stats
from google.appengine.api import users
from google.appengine.ext.webapp import template
from twilio import twiml

"""
This class acts a call agent and responds to calls from Twilio service.
It reads the latest measurement, assembles a voice.xml string and
sends it back to the Twilio server.
"""

class CallAgent():
	def post(self, handler):
		
		converter = Converter()
		measurements_query = Measurement.query().order(-Measurement.date)
		"""
		We only fetch the latest data point
		"""
		points = measurements_query.fetch(1)
		"""
		To do: error check if any data was returned
		error cause: empty database 
		"""
		
		resultString = ''				
		resultString += "Letzter Messwert: "
		temp = converter.asciiToFloat(points[0].temperature)
		resultString += "Temperatur %2.1f Grad." % converter.convertToDegree(temp)

		r = twiml.Response()
		r.say(resultString, voice="male", language="de")
		handler.response.headers['Content-Type'] = 'text/xml'
		handler.response.write(str(r))


	def get(self, handler):
		
		converter = Converter()
		measurements_query = Measurement.query().order(-Measurement.date)
		"""
		We only fetch the latest data point
		"""
		points = measurements_query.fetch(1)
		"""
		To do: error check if any data was returned
		error cause: empty database 
		"""
		
		resultString = ''				
		resultString += "Letzter Messwert "
		temp = converter.asciiToFloat(points[0].temperature)
		resultString += "Temperatur %2.1f Grad." % converter.convertToDegree(temp)

		r = twiml.Response()
		r.say(resultString, voice="male", language="de")
		handler.response.headers['Content-Type'] = 'text/xml'
		handler.response.write(str(r))
