# Listens for door contact
# Triggers callback for door close/open

class DoorSocketListener:
	GPIO_PIN = 5
	def __init__(self, callback_close, callback_open)
		self.callback_open = callback_open
		self.callback_close = callback_close
		# True - open, False - closed
		self.state = self.check_state()

	def toggle():
		self.state = !self.state

	def listen(self):
		if self.state:
			# todo initiate listening for close
		else:
			# todo initiate listening for open

	def check_state(self):
		# check if door is open or closed
		return bool
