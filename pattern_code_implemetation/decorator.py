from functools import wraps

def make_blink(function):
	""" Defines the decorator """

	# This makes the decorator transparent in terms of its name and docstring 
	@wraps(function)

	# Define the inner function
	def decorator():
		# grab  the return value of the function being decorated
		ret = function()
		# add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>"

	return decorator

@make_blink
def helloworld():
	""" Original function """
	return "hello, world!"

# check if the function name is still the same name for the function decorated
print(helloworld.__name__)
# check if the docstring is still the same for the function being decorated
print(helloworld.__doc__)

# decorated function returns <blink> ...
print(helloworld())