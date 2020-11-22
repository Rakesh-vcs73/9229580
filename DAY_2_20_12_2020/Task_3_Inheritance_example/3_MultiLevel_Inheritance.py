class Building:
	def __init__(self,location):
		self.location=location
	def details(self):
		print("Location : ",self.location)

class Apartment(Building):
	def __init__(self,location,apt_no,resident):
		self.resident=resident
		self.apt_no=apt_no
		Building.__init__(self,location)
	def details(self):
		Building.details(self)
		print("Apartment number",self.apt_no)
		print("Current Resident : ",self.resident)

class Home(Apartment):
	def __init__(self,location,apt_no,resident,no_of_rooms):
		self.no_of_rooms=no_of_rooms
		Apartment.__init__(self,location,apt_no,resident)
	def details(self):
		Apartment.details(self)
		print("Number of rooms : ",self.no_of_rooms)


home1 = Home("Bangalore",10,"Chandler",3)
home1.details()
