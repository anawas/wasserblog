import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext.webapp import template


class Renderer(webapp2.RequestHandler):
	"""
	Renders a template 
	"""
	def doRender(self, handler, tname = 'index.html', values = {}):
		temp = os.path.join(
			os.path.dirname(__file__),
			'templates/' + tname)
		
		if not os.path.isfile(temp):
			return False

		#make a copy of the dictionary and add the path
		newval = dict(values)
		newval['path'] = handler.request.path

		outstr = template.render(temp, newval)
		handler.response.out.write(outstr)
		return True
