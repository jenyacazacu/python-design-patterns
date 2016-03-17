class Subject(object): #Represents what is being observed
	def __init__(self):
		self._observers = [] # this is where references to all observers are being kept
							 # This is one-to-many relationship : there will be one subject to be observed by multiple observ

	def attach(self, observer):
		if observer not in self._observers: # if the observer is not already in the list attach it
			self._observers.append(observer) # append the observer to the list
		

	def detach(self, observer):
		try:	# detach the observer from the list
			self._observers.remove(observer)
		except ValueError:
			pass
	def notify(self, modifier=None):
		for observer in self._observers: #for all the observers in the list
			if modifier != observer: # dont notify the observer that is updating the temperature
				observer.update(self) # alert the observers

class Core(Subject): # Inherits from the subject
	
	def __init__(self, name=""):
		Subject.__init__(self)
		self._name = name # set the name of the core
		self._temp = 0 # initialize the temperature

	@property # getter that gets the core temperatures
	def temp(self):
	    return self._temp

	@temp.setter # setter that sets the core temperature
	def temp(self, temp):
		self._temp = temp
		# notify the observers when somebody changes the core temperature
		self.notify()

class TempViewer:

	def update(self, subject): # alert method that is invoked when the notify() method in a concrete subject is invoked
		print('Temperature Viewer: {} has Temperature {}'.format(subject._name, subject._temp))

# create the subjects
c1 = Core("Core1")
c2 = Core("Core2")

# create observer
v1 = TempViewer()
v2 = TempViewer()

# attach
c1.attach(v1)
c1.attach(v2)

# change temp
c1.temp = 80
c1.temp = 90



	

