from machine.state import State

import configparser
import math







class Machine:
	def __init__(self, length, time_step, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__length    = length
		self.__time_step = time_step
		
		
		
		
		
	@property
	def length(self):
		return self.__length
		
		
		
	@property
	def time_step(self):
		return self.__time_step
		
		
		
		
		
	def compute_trajectory(self, state, controls_sequence):
		x, y, orientation = state.coordinates
		trajectory_time   = 0.0
		
		
		yield trajectory_time, state
		
		for control in controls_sequence:
			velocity, angle       = control.velocity, control.angle
			residual_control_time = control.duration
			
			while residual_control_time > 0.0:
				x += velocity * math.cos(orientation) * self.__time_step
				y += velocity * math.sin(orientation) * self.__time_step
				
				orientation += \
					velocity / self.__length * math.tan(angle) \
						* self.__time_step
						
						
				trajectory_time, residual_control_time = \
					trajectory_time + self.__time_step, \
						residual_control_time - self.__time_step
						
				state = State([x, y, orientation])
				
				
				yield trajectory_time, state
				
				
				
				
				
				
				
def load_machine(config_file):
	def create_machine(parser):
		try:
			length    = parser.getfloat("DEFAULT", "MachineLength")
			time_step = parser.getfloat("DEFAULT", "TimeStep")
		except:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		machine = Machine(length, time_step)
		
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
	