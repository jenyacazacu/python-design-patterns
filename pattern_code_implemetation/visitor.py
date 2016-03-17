class House(object):
	def accept(self, visitor):
		visitor.visit(self)

	def work_on_hvac(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist)

	def work_on_electricity(self, electricity_specialist):
		print(self, "worked on by", electricity_specialist)

	def __str__(self):
		return self.__class__.__name__

class Visitor(object):
	def __str__(self):
		return self.__class__.__name__

class HvacSpecialist(Visitor):
	def visit(self, house):
		house.work_on_hvac(self)

class ElectricalSpecialist(Visitor):
	def visit(self, house):
		house.work_on_electricity(self)

# create hvac spec
hvac_spec = HvacSpecialist()
#create electrician
electr_spec = ElectricalSpecialist()
# create a house
house = House()
# accept
house.accept(hvac_spec)
house.accept(electr_spec)