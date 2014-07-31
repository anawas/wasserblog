import webapp2
import os
import logging
from Renderer import Renderer
from Measurement import Measurement
from Converter import Converter
from google.appengine.ext import ndb
from google.appengine.ext.db import stats
from google.appengine.api import users
from google.appengine.ext.webapp import template


"""
This class reads the values from the Datastore and
renders them into an HTML table
"""
class Analyzer():
		
	""" 
	This methods mimics the get method of a webapp2.RequestHandler.
	Such an object is passed with the handler argument
	"""
	def get(self, handler):
		converter = Converter()
		
		measurements_query = Measurement.query().order(-Measurement.date)
		points = measurements_query.fetch(20)
		resultString = ''
		stringToRender = {}
		
		global_stats = stats.GlobalStat.all().get()
		
		stringToRender['stats'] = "<p>Total entities stored %d</p>" % global_stats.count
		
		for point in points:
			resultString += "<tr>\n"
			resultString += "<td>%s</td> " % point.date
			resultString += "<td>%s</td> " % point.brightness
			temp = converter.asciiToFloat(point.temperature)
			resultString += "<td>%2.1f *C</td>\n" % converter.convertToDegree(temp)
			resultString += "</tr>\n"

		stringToRender['results'] = resultString
		render = Renderer()
		render.doRender(handler, 'results.html', stringToRender)
		
