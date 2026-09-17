import random
from prox import switches
from database import get_conn

#name=input("Enter the Name of the Switch station being initialized: ")
#country=input("Enter Country of operation of the Switch station: ")
#ccode=int(input("Enter Official Country code for the Country of Operation: "))

class MSC:

	def __init__(self, ccode, country):

		#self.name=name
		self.ccode=ccode
		self.country=country

	# def info(self):
	# 	info=f"This is MSC {self.name} with Country code +{self.ccode}"
	# 	print(info)
	# 	return info

	def create(self):

		conn=get_conn()

		degree=round(random.uniform(34, 42), 1)
		#orientation=random.choice(["N", "S"])
		ordinate=round(random.uniform(-4.5, 4.5), 1)
		elevation=random.randrange(0, 6100, 5)
		
		if ordinate < 0.0:
			orientation="S"
		else:
			orientation="N"


		latitude=f"{ordinate}{orientation}"
		longitude=f"{degree}E"
		altitude=f"{elevation} Feet"

		#this is where the per-province assignment is done
		"""
		boundaries=[
    		-1.16, -1.44, 37.10, 36.65, Nairobi,
    		-0.20, -1.30, 37.60, 36.40, Central,
    		-1.60, -4.70, 41.90, 38.00, Coast,
    		4.00, -3.00, 40.00, 37.00, Eastern,
    		4.00, -1.50, 41.90, 38.00, North Eastern,
    		0.20, -1.50, 35.30, 33.90, Nyanza,
    		4.50, -3.00, 37.00, 34.80, Rift Valley,
    		1.10, 0.00, 35.00, 33.90, Western
				]
		"""


		if (-1.44 <= ordinate <= -1.16) and (36.65 <= degree <= 37.10):
			name = "Nairobi"

		elif (-1.30 <= ordinate <= -0.20) and (36.40 <= degree <= 37.60):
			name = "Central"

		elif (-4.70 <= ordinate <= -1.60) and (38.00 <= degree <= 41.90):
			name = "Coast"

		elif (-3.00 <= ordinate <= 4.00) and (37.00 <= degree <= 40.00):
			name = "Eastern"

		elif (-1.50 <= ordinate <= 4.00) and (38.00 <= degree <= 41.90):
			name = "North Eastern"

		elif (-1.50 <= ordinate <= 0.20) and (33.90 <= degree <= 35.30):
			name = "Nyanza"

		elif (-3.00 <= ordinate <= 4.50) and (34.80 <= degree <= 37.00):
			name = "Rift Valley"

		elif (0.00 <= ordinate <= 1.10) and (33.90 <= degree <= 35.00):
			name = "Western"

		else:
			name = "Support"


		# name=name
		country=self.country
		country_code=self.ccode


		cursor=conn.cursor()

		data = switches()
		if name in data:
			print(f"{name} switch already commissioned")
		else:
			cursor.execute(
				"INSERT INTO switch (name, latitude, longitude, altitude, country, country_code) VALUES (?, ?, ?, ?, ?, ?)",
				(name, latitude, longitude, altitude, country, country_code)
					)
			confirmation=f"{name} switch comissioned successfully"
			print(confirmation)


		conn.commit()
		conn.close()

#station=MSC(name, ccode, country)
#station.info()
#station.create()
