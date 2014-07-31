import webapp2
import os
import math
import logging
from Analyzer import Analyzer
from Measurement import Measurement
from CallAgent import CallAgent
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

"""
This class handles the GET from /analyze
It calls its delegate 'Analyzer' which processes and renders the
data in the Datastore.
"""
class AnalyzeHandler(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		
		if user:
			analyzer = Analyzer()
			analyzer.get(self)
		else:
			self.redirect(users.create_login_url(self.request.uri))

"""
This class handles the POST request from the board
"""
class MeasurementHandler(webapp2.RequestHandler):
	def post(self):
		measure = Measurement()
		measure.brightness = self.request.get('bright')
		measure.temperature = self.request.get('temp')
		measure.put()


"""
This class handles requests from Twilio. We don't care
if there's a post or get request.
"""
class CallAgentHandler(webapp2.RequestHandler):
	def get(self):
		agent = CallAgent()
		agent.get(self)

	def post(self):
		agent = CallAgent()
		agent.post(self)

"""
This class renders the standard web page at "/"
Replace this with appropriate content
"""
class MainPage(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		
		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write('Hello, World!')
		else:
			self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/analyze', AnalyzeHandler),
	('/measure', MeasurementHandler),
	('/tell', CallAgentHandler)
], debug=True)

def main():
	logging.getLogger().setLevel(logging.DEBUG)
	wabapp.util.run_wsgi_app(application)
	
if __name__ == '__main__':
	main()
