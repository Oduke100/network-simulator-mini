from switch import MSC
from models import init_db
from router import s_all, s_specific, s_remove

init_db()

try:
	while True:
		command=input("nsm >>> ")

		parts=command.split()
		parts[0].lower()

		if parts[0]=="gall":
			switch=s_all()
			print(switch)

		elif parts[0]=="specific":
			switch=s_specific(parts[1])
			print(switch)

		elif parts[0]=="rem":
			s_remove(parts[1])
			print(f"{parts[1]} switch decomissioned successfully")

		elif parts[0]=="set":
			station=MSC(parts[1], parts[2])
			station.create()
			# confirmation="switch created successfully"
			# print(confirmation)

		elif parts[0]=="exit":
			break

except KeyboardInterrupt:
		print("\n Exiting Gracefully.... ")
