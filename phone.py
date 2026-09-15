class Phone:
	def __init__(self, battery):
		self.battery=battery

	def check_battery(self):
		print(f"Your battery Level is {self.battery}")

samsung=Phone("90%")
samsung.check_battery()
