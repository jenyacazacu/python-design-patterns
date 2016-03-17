
# initial
class Dog:
	"""A simple class Dog """
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"


# This factory method allows us to later add a class easily
def get_pet(pet="dog"):
	""" The facroty method used to create out object """
	# initial
	# pets = dict(dog=Dog("hope"))
	
	# modified
	pets = dict(dog=Dog("Hope"), cat=Cat("Soul"))
	return pets[pet]

# additional
class Cat:
	"""A simple class Dog """
	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"

dog = get_pet("dog")
print(dog.speak())

cat = get_pet("cat")
print(cat.speak())