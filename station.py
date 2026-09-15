from switch import country, location, ccode

class Station:
	def __init__(self, location, ccode):
		self.location=location
		self.ccode=ccode

	def check_location(self):
		info=f"The location of this site is {self.location} and Country code used is +{self.ccode}"
		return info

juja=Station(location, ccode)
juja.check_location()
