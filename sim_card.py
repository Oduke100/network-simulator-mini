from station import location, ccode, location

number=int(input("Enter the number you want: "))

class Card:
	def __init__(self, ccode, number, location):
		self.number=number
		self.ccode=ccode
		self.location=location

	def check_number(self):

		phone_number=f"+{self.ccode}{self.number}"

		print(f"Your phone number is: {phone_number}")

safaricom=Card(ccode, number, location)
safaricom.check_number()
