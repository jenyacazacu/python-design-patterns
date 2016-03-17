class Dog:
	""" One of the objects to be returned """
	def speak(self):
		return "Woof!"
	def __str__(self):
		return "Dog"

class DogFactory:
	"""Concrete Factory"""
	def get_pet(self):
		"""return a dog object"""
		return Dog()

	def get_food(self):
		"""return a dog food object"""
		return "Dog Food"

class PetStore:
	""" pet store houses our abstract factory"""
	def __init__(self, pet_factory=None):
		""" pet_factory is our abstract factory """
		self._pet_factory = pet_factory
	def show_pet(self):
		"""Utility method  to display the details of the object  returned by the DogFactory"""
		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("our pet is '{}'".format(pet))
		print("our pet says hello by '{}'".format(pet.speak()))	
		print("its food is '{}'".format(pet_food))

# Create a concrete factory
factory = DogFactory()

# create a pet store housing our  Abstract Factory
shop = PetStore(factory)

# invoke the utility method 
shop.show_pet()