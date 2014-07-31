import webapp2
import os
import logging
from Converter import Converter
from Measurement import Measurement
from google.appengine.ext import ndb
from google.appengine.ext.db import stats
from google.appengine.api import users
from google.appengine.ext.webapp import template
from twilio.rest import TwilioRestClient

"""
This class acts a call agent and responds to calls from Twilio service.
It reads the latest measurement, assembles a voice.xml string and
sends it back to the Twilio server.
"""

class CallAgent():
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
		resultString += "Latest measurement is "
		temp = converter.asciiToFloat(points[0].temperature)
		resultString += "temperature %2.1f degrees centigrades." % converter.convertToDegree(temp)

		handler.response.headers['Content-Type'] = 'text/plain'
		handler.response.write('This is CallAgent answering your call!\n')
		handler.response.write('My answer is: %s' % resultString)


		account_sid = "ACcd3e6b7eafbb0166ab5e6f95b44ec19e"
		auth_token  = "4b6ef0e7bb2aa154747d8b6b028a381a"
		client = TwilioRestClient(account_sid, auth_token)
 
"""
		call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    		to="+41612670909",    # Replace with your phone number
    		from_="+41435084611", # Replace with your Twilio number,
    		timeout="30")		  # ring for 30 s
		print call.sid
"""