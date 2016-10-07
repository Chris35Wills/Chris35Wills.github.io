# help with properties: http://www.python-course.eu/python3_properties.php

class dog_complex:
	"A customisable dog"
	
	def __init__(self, size, weight, height):

		self.Kingdom = "Animalia"
		self.Phylum = "Chordata"
		self.Clade = "Synapsida"
		self.Class = "Mammalia"
		self.Order = "Carnivora"
		self.Suborder = "Caniformia"
		self.Family = "Canidae"
		self.Genus = "Canis"
		self.Species = "C. lupus"
		self.Subspecies = "C. l. familiaris"

		if type(size) != str:
			print("size must be of str type e.g. 'medium'")
		else:
			self.size=size

		if type(weight) != float:
			print("weight must be of float type (representing kg) e.g. 12")
		else:
			self.weight=weight
		
		if type(height) != float:
			print("weight must be of float type (representing m) e.g. 0.5")
		else:
			self.height=height 
		
	def bark(self):

		"Make the dog bark"

		print("Woof!")

	def growl(self):
		
		"Make the dog growl"

		print("Grrr")

	@property
	def weight(self):
		return self.__weight

	@weight.setter
	def weight(self, value):
		if type(value) != float:
			print("Weight must be declared as a float (kg)")
		else:
			self.__weight = value

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		if type(value) != str:
			"size must be declared as a string - something like 'small' or 'medium'"
		else:
			self.__size = value
			
	@property
	def height(self):
		return self.__height
			
	@height.setter
	def height(self, value):
		if type(value) == str:
			"height must be declared as a float in metres, not a string"
		else:
			self.__height = value
	
	def FoodCostPerWeek(self):
		"Estimate of food cost per week based on weight in kg"

		if (self.weight <= 5):
			print("£10")
		elif (self.weight >= 5) and (self.weight <= 10):
			print("£20")
		elif (self.weight >= 10) and (self.weight<= 20):
			print("£30")
		elif (self.weight >= 20) and (self.weight <= 40):
			print("£40")
		elif (self.weight >= 40):
			print("£50 +")