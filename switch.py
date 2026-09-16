import random
from database import get_conn

#name=input("Enter the Name of the Switch station being initialized: ")
#country=input("Enter Country of operation of the Switch station: ")
#ccode=int(input("Enter Official Country code for the Country of Operation: "))

class MSC:

	def __init__(self, name, ccode, country):
		self.name=name
		self.ccode=ccode
		self.country=country

	def info(self):
		info=f"This is MSC {self.name} with Country code +{self.ccode}"
		print(info)
		return info

	def create(self):

		conn=get_conn()

		degree=round(random.uniform(34, 42), 1)
		#orientation=random.choice(["N", "S"])
		ordinate=round(random.uniform(-4.5, 4.5), 1)
		elevation=random.randrange(0, 6100, 5)
		if ordinate < 0:
			orientation="S"
		else:
			orientation="N"


		latitude=f"{ordinate}{orientation}"
		longitude=f"{degree}E"
		altitude=f"{elevation} Feet"
		name=self.name
		country=self.country
		country_code=self.ccode


		cursor=conn.cursor()
		cursor.execute(
			"INSERT INTO switch (name, latitude, longitude, altitude, country, country_code) VALUES (?, ?, ?, ?, ?, ?)",
			(name, latitude, longitude, altitude, country, country_code)
				)

		conn.commit()
		conn.close()
		#confirmation=f"{self.name} switch created successfully"
		#return confirmation
		#print(confirmation)

#station=MSC(name, ccode, country)
#station.info()
#station.create()
