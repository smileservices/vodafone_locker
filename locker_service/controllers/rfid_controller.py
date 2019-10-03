import mercury

class RfidController:
	GPIO_PIN = 15

	@classmethod
	def scan()
		'''
		scan multiple times and hold the tags in a set
		return iterable
		'''
		reader = mercury.Reader('tmr:///dev/ttyUSB0')
		reader.set_region('EU3')
		reader.set_read_plan([1], 'GEN2')
		tags_set = {}
		for _ in range(10)
			for tag in reader.read():
				tags_set.add(tag)
		return tags_set