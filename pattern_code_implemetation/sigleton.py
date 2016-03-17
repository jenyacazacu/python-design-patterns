class Borg:
	""" Borg class making class attribute global"""
	_shared_state = {} # Attribute dictionary

	def __init__(self):
		self.__dict__ = self._shared_state # make it an  attribute dictionary

class Singleton(Borg):
	"""The class shares all its attributes among its various instances """
	#this esentially makes the singleton object an object oriented global variable

	def __init__(self, **kwargs):
		Borg.__init__(self)
		# update the attribute dictionary by inserting a new key_value pair
		self._shared_state.update(kwargs)

	def __str__(self):
		# Returns the attribute dictionary for printing
		return str(self._shared_state)

# Create a singleton object and add forst entry
s = Singleton(HTTP = "Hyper Text Tranfer Protocol")
print(s)

s2 = Singleton(SNMP = "Simple Network Management Protocol")
print(s2)
