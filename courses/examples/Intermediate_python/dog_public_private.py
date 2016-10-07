# help with properties: http://www.python-course.eu/python3_properties.php

class dog_public_private:
	"""
	A customisable dog with public and private properties

	Example:

	d=dog(23)
	d.Kingdom # Animalia
	d.Kingdom=None # set Kingdom to None type - DANGER!! (e.g. if this was a bank account and 'balance' was initialised in this way, you could set it to zero!)

	d.__weight # not accessible!!
	d.weight # 23 # only accessbile due to presence of property methods
	d.weight = 18 # only possible to change it due to setter property method

	"""
	
	def __init__(self, weight):

		self.Kingdom = "Animalia" # 'public' variable

		self.__weight=weight # 'private variable' - can only be changed using properties and the associated getter/setter methods
		
	@property
	def weight(self):
		return self.__weight

	@weight.setter
	def weight(self, value):
		if type(value) != float:
			print("Weight must be declared as a float (kg)")
		else:
			self.__weight = value

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