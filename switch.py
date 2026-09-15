location=input("Enter the Name of the Switch station being initialized: ")
country=input("Enter Country of operation of the Switch station: ")
ccode=int(input("Enter Official Country code for the Country of Operation: "))

class MSC:

	def __init__(self, location, ccode):
		self.location=location
		self.ccode=ccode

	def info(self):
		info=f"This is MSC {self.location} with Country code +{self.ccode}"
		return info

Thika=MSC(location, ccode)
Thika.info()
