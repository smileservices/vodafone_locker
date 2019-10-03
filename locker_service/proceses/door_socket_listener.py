import RPi.GPIO as GPIO
from time import sleep


# Listens for door contact
# Triggers callback for door close/open

class DoorSocketListener:
	GPIO_PIN = 5
	var = 1
	door = 12

	def __init__(self, callback_close, callback_open)
		self.callback_open = callback_open
		self.callback_close = callback_close

	def callback():
		if self.var == 1:
			#sleep(1.5)  # confirm the door is opened by waiting 1.5 sec 
			if GPIO.input(self.door) == 1: # and check again the input
				self.callback_open()
	            # stop detection for 10 sec
				#GPIO.remove_event_detect(door)
				#sleep(10)
				#GPIO.add_event_detect(door, GPIO.RISING, callback=my_callback, bouncetime=300)
			else:
				self.callback_close()
				#start RFID scanning
		#GPIO.cleanup()

	def listen(self):
		var=1
		door = 12
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(door, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(door, GPIO.RISING, callback=self.callback, bouncetime=300)
