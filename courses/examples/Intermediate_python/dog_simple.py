# help with properties: http://www.python-course.eu/python3_properties.php

class dog_simple:
	"A customisable dog - needs a size, weight and height"
	
	def __init__(self, size, weight, height):

		# 'public' variables...
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

