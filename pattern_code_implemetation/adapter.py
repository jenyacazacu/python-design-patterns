class Korean:
	"""Korean Speaker"""
	def __init__(self):
		self.name = "Korean"
	def speak_korean(self):
		return "Speaks Korean"

class British:
	"""English Speaker"""
	def __init__(self):
		self.name = "British"
	def speak_english(self):
		return "Speaks English"

class Adapter:
	"""This changes the individualized method names to generic method name"""

	def __init__(self, object, **adapted_method):
		"""Change the name of the method"""
		self._object = object

		#add a new dictionary that establishes the mapping between the generic method name: speak() and the concrete method
		#for example:speak() will be translated to speak_korean() if the dict says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""Simply return the rest of attributes"""
		return getattr(self._object, attr)
# lsit the store speaker object
objects = []

korean = Korean()
british = British()

objects.append(Adapter(korean,speak = korean.speak_korean))
objects.append(Adapter(british,speak=british.speak_english))

for obj in objects:
	print('{} says {}'.format(obj.name, obj.speak()))

