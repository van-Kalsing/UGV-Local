from machine.machine import Machine, MachineState

import configparser







def load_machine(config_file):
	def create_machine(parser):
		try:
			machine_length = parser.getfloat("DEFAULT", "MachineLength")
			time_step      = parser.getfloat("DEFAULT", "TimeStep")
		except:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		machine = \
			Machine(
				length    = machine_length,
				time_step = time_step
			)
			
		return machine
		
		
		
	parser = configparser.ConfigParser()
	
	
	try:
		parser.read_file(config_file)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	try:
		machine = create_machine(parser)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	return machine
	