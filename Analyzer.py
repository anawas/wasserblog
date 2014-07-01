import webapp2
import os
import math
import logging
from Renderer import Renderer
from Measurement import Measurement
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
	Helper function to convert an ASCII string into a float
	"""
	def asciiToFloat(self, ascnumber):
		res = float(ascnumber)
		return res
		
	"""
	Helper function to convert a float into a string.
	"""
	def floatToAscii(self, floatnumber):
		res = "%2.2f" % floatnumber
		return res
		
	"""
	Converts the raw thermistor readout in Datastore to a temperature
	in *C
	"""
	def convertToDegree(self, number):
		tempInDeg = number / 10000.0
		tempInDeg = math.log10(tempInDeg)
		tempInDeg /= 3950.0
		tempInDeg += 1.0 / (25.0 + 273.15)
		tempInDeg = 1.0 / tempInDeg
		tempInDeg -= 273.15		
		return tempInDeg 

	"""
	Converts a temperature in *C to *F
	"""
	def convertToFahrenheit(self, number):
		res = number * 1.8
		res += 32
		return res
		
	""" 
	This methods mimics the get method of a webapp2.RequestHandler.
	Such an object is passed with the handler argument
	"""
	def get(self, handler):
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
			temp = self.asciiToFloat(point.temperature)
			resultString += "<td>%2.1f *C</td>\n" % self.convertToDegree(temp)
			resultString += "</tr>\n"

		stringToRender['results'] = resultString
		render = Renderer()
		render.doRender(handler, 'results.html', stringToRender)
		
