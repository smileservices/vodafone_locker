import requests
from processes import BadgeSocketListener, DoorSocketListener
from controllers import DoorController, RfidController

REST_API_ENDPOINT = ''
API_KEY = ''

class MainController:
	"""docstring for MainController"""
	def __init__(self, door_controler, rfid_controller):
		self.door_controler = door_controler
		self.rfid_controller = rfid_controller
		#todo initiate badge socker listener
		self.badge_listener = BadgeSocketListener(self.validate_badge)
		#initiate door socker listener
		self.door_listener = DoorSocketListener(self.open_door, self.close_door)
		self.door_listener.listen()

	def validate_badge(badge_id):
		response = self.send_data('badge_id', badge_id)
		if response['valid']:
			self.door_controler.open()

	def inspect_locker_content():
		tags = self.rfid_controller.scan()
		response = self.send_data('tags', [tag for tag in tags])

	def open_door():
		# do something ... log?
		pass

	def close_door():
		self.inspect_locker_content()

	def send_data(self, key, data):
		data = {
			'api_key': API_KEY,
			key: data
		}
		#todo set authentication header 
		r = requests.post(REST_API_ENDPOINT, data=data)
		response = r.json()
		return response


mainController = MainController(
	DoorController,
	RfidController
	)
badgeListener = BadgeSocketListener(
	mainController.validate_badge
	)
doorListener = DoorSocketListener(
	mainController.inspect_locker_content(),
	mainController.open_door()
	)