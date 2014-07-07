from visualization.visualizer import Visualizer

import configparser







def load_visualizer(config_file):
	def create_visualizer(parser):
		try:
			machine_length = parser.getfloat("DEFAULT", "MachineLength")
			machine_width  = parser.getfloat("DEFAULT", "MachineWidth")
			time_interval  = parser.getfloat("DEFAULT", "TimeInterval")
		except:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		visualizer = \
			Visualizer(
				machine_size  = (machine_length, machine_width),
				time_interval = time_interval
			)
			
		return visualizer
		
		
		
	parser = configparser.ConfigParser()
	
	
	try:
		parser.read_file(config_file)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	try:
		visualizer = create_visualizer(parser)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	return visualizer
	