class DrawingAPIOne(object):
	"""Implementation specific abstraction concrete class one"""
	def draw_circle(self, x, y, radius):
		print('API 1 drawing a circle at ({0},{1} with radius {2}!)'.format(x,y,radius))

class DrawingAPITwo(object):
	"""Implementation specific abstraction concrete class one"""
	def draw_circle(self, x, y, radius):
		print('API 2 drawing a circle at ({0},{1} with radius {2}!)'.format(x,y,radius))

class Circle(object):
	"""Implementation-independent abstration for example there could be a rectangle class"""

	def __init__(self, x, y, radius, drawing_api):
		"""initialize the necessary attributes """
		self._x = x
		self._y = y
		self._radius = radius
		self._drawing_api = drawing_api

	def draw(self):
		"""Implementation specific abstraction taken care of by another class: DrawingApi"""
		self._drawing_api.draw_circle(self._x, self._y, self._radius)

	def scale(self, percent):
		self._radius *= percent

#test
circle1 = Circle(1,2,3,DrawingAPIOne())
#draw the circle
circle1.draw()

# build with api2 ..
circle2 = Circle(1,2,3,DrawingAPITwo())
#draw the circle
circle2.draw()