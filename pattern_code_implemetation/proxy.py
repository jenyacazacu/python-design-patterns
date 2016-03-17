import time

class Producer:
	""" Define the resource intensive producer """
	def produce(self):
		print('Producer is working hard')

	def meet(self):
		print("The producer is ready to meet you")

class Proxy:
	""" Define the less intensive proxy that only instantiates producer when necessary """
	def __init__(self):
		self.occupied = "No"
		self.producer = None

	def produce(self):
		""" Check if producer is available """
		print("Artist checking if producer is available...")
		if self.occupied == "No":
			self.producer = Producer()
			time.sleep(2)

			#make the producer meet the quest
			self.producer.meet()
		else:
			#otherwise dont instantiate a producer
			time.sleep(2)
			print('Producer is busy')
#instantiate a proxy
proxy = Proxy()
#Make the proxy: Artist produce until Producer is vailable
proxy.produce()

#change the state to occupied
proxy.occupied = 'Yes'
#try to produce
proxy.produce()