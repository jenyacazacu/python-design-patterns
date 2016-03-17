def count_to(count):
	"""Iterator implementation"""
	# the list
	number_in_romanian = ['unu','doi','trei','patru','cinci']

	#the built in iterator
	#create a tuple such as ('1','unu')
	iterator = zip(range(count),number_in_romanian)

	#iterate through the iterable list
	#extract the romanian numbers
	#run them in a generator called number
	for position, number in iterator:

		# return a 'generator' containing numbers in romanian
		yield number

#testing
for num in count_to(3):
	print('{}'.format(num))