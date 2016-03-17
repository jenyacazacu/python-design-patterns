import types

class Strategy:
	"""The Strategy Pattern Class"""
	def __init__(self, function=None):
		self.name = "Default Strategy"

		#if a reference to a function is provided replace the execute() function with the given function
		if function:
			self.execute = types.MethodType(function, self)

	def execute(self):
		"""The defautl method that prints the strategy being used"""
		print("{} is being used".format(self.name))

def strategy_one(self):
	print("{} is used to execute method 1".format(self.name))

def strategy_two(self):
	print("{} is used to execute method 2".format(self.name))

#create a default strategy
s0 = Strategy()
#execute the default strategy
s0.execute()

#variations
s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

s1 = Strategy(strategy_two)
s1.name = "Strategy Two"
s1.execute()



