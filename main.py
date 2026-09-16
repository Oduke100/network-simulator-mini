from switch import MSC
from database import init_db
from router import all, specific, remove

init_db()

try:
	while True:
		command=input("nsm >>> ")

		parts=command.split()
		parts[0].lower()

		if parts[0]=="gall":
			switch=all()
			print(switch)

		elif parts[0]=="specific":
			switch=specific(parts[1])
			print(switch)

		elif parts[0]=="rem":
			remove(parts[1])
			print(f"{parts[1]} switch decomissioned successfully")

		elif parts[0]=="set":
			station=MSC(parts[1], parts[2], parts[3])
			station.create()
			confirmation=f"{parts[1]} switch created successfully"
			print(confirmation)

		elif parts[0]=="exit":
			break

except KeyboardInterrupt:
		print("\n Exiting Gracefully.... ")
