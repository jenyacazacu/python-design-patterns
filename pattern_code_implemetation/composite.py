class Component(object):
	"""Abstarct Class"""
	def __init__(self, *args, **kwargs):
		pass
	def component_function(self):
		pass

class Child(Component):
	"""Concrete class"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#this is where we store the name of the child class
		self.name = args[0]

	def component_function(self):
		#print the name of your child function here
		print('{}'.format(self.name))

class Composite(Component):
	"""Concrete class and maintains the tree recursive structure"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#this is where we store the name of the composite object
		self.name = args[0]

		#this is where we keep our child objects
		self.children = []

	def append_child(self, child):
		"""Method to add a new child item"""
		self.children.append(child)

	def remove_child(self, child):
		"""Method to remove a given child"""
		self.children.remove(child)

	def component_function(self):

		#print the name of the composite object
		print("{}".format(self.name))

		#iterate through the child objects and and invoke their component function priting their name
		for i in self.children:
			i.component_function()

#build a composite submenu1
sub1 = Composite("submenu1")

#create a new child sub_submenu11
sub11 = Child('sub_submenu11')
#create a new child sub_submenu11
sub12 = Child('sub_submenu12')

#add the children to composite
sub1.append_child(sub11)
sub1.append_child(sub12)

#built a top level 
top = Composite('top_menu')

#build a submenu 2 that is not a composite
sub2 = Child('sub_menu2') 

top.append_child(sub1)
top.append_child(sub2)

#test
top.component_function()

