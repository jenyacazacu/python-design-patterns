class Handler: #Abstract handler
	"""Abstract hadler"""
	def __init__(self, successor):
		self._successor = successor #define who is the next handler
	
	def handle(self, request):
		handled = self._handle(request) # if handled stop here 

		#otherwise keep going
		if not handled:
			self._successor.handle(request)
	def _hanle(self, request):
		raise NotImplementedError('Must provide implementation is subclass')

class ConcreteHandler(Handler):
	"""Concrete handler 1"""
	def _handle(self, request):
		if 0 < request <=10: #provide a condition for handling
			print('request {} handled in handler 1'.format(request))
			return True
class DefaultHandler(Handler):
	"""Default handler """

	def _handle(self, request):
		"""If there is not handler available"""
		print('rend of chain no handler for {}'.format(request))
		return True

class Client(object): #using handlers
	def __init__(self):
		self.handler = ConcreteHandler(DefaultHandler(None)) #create handlers and use them in a sequesnce you want

	def delegate(self, requsts):
		for request in requests:
			self.handler.handle(request)

#create a client
c = Client()
requests = [2, 5, 30]
c.delegate(requests)







