import random
from map import boundaries
from database import get_conn
from switch import country, location, ccode

class Station:
	def __init__(self, location, ccode):
		self.location=location
		self.ccode=ccode

	def check_location(self):
		info=f"The location of this site is {self.location} and Country code used is +{self.ccode}"
		return info

	def create(self):

		conn=get_conn()
		cursor=conn.cursor()

		degree=round(random.uniform(34, 42), 1)
		ordinate=round(random.uniform(-4.5, 4.5), 1)
		elevation=random.randrange(0, 6100, 5)
		
		if ordinate < 0.0:
			orientation="S"
		else:
			orientation="N"


		latitude=f"{ordinate}{orientation}"
		longitude=f"{degree}E"
		altitude=f"{elevation} Feet"

		cursor.execute(
			"INSERT INTO station (name, latitude, longitude, altitude, switch_id)"
		)
juja=Station(location, ccode)
juja.check_location()
