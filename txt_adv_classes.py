class Room():
	#base class for rooms
	def __init__(self, name, description, items):
		self.name = name
		self.description = description
		self.items = items

	def info(self):
		print ('\nYou are now inside of:', self.name)
		print (self.description)

class Labos(Room):
	def __init__(self):
		super().__init__(name='The lab', description='There are many undiscovered items in here!', items = ['microscope', 'SUPER SECRET RESEARCH NOTES', 'knife', 'suspicious pills'])


class Player():
	#the player class with name location and inventory
	def __init__(self, name, location, items):
		self.name = name
		self.location = location
		self.items = []

# a method for looting items
	def take_item (self, item_name, room_name):
		#self = passed_object
		if(item_name in room_name.items):
			room_name.items.remove(item_name)
			self.items.append(item_name)


