# Instantiate and run process for detecting badge reading
# 
# Initialization starts process for listening on badge read event
# Badge read event sends signal

class BadgeSocketListener:
	GPIO_PIN = 12

	def __init__(self, callback):
		self.start_listening_badge_read(callback)

	def start_listening_badge_read(callback):
		# todo start process for listening on pin signal
		pass