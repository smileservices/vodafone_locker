# Instantiate and run process for detecting badge reading
# 
# Initialization starts process for listening on badge read event
# Badge read event sends signal

class BadgeSocketListener:
	GPIO_PIN = 12

	def __init__(self, callback):
		self.callback = callback

	def listen():
		# todo start process for listening on pin signal
		pass