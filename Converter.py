import math

"""
Helper class to convert 
	string <--> numbers, 
	raw sensor readings --> temperature
	*C <--> *F
"""
class Converter():
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

