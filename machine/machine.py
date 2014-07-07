import math







class MachineState:
	def __init__(self, coordinates, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__coordinates = tuple(coordinates)
		
		
		
	@property
	def coordinates(self):
		return self.__coordinates
		
		
		
		
		
		
		
class MachineControl:
	def __init__(self, velocity, angle, duration, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__velocity = velocity
		self.__angle    = angle
		self.__duration = duration
		
		
		
		
		
	@property
	def velocity(self):
		return self.__velocity
		
		
		
	@property
	def angle(self):
		return self.__angle
		
		
		
	@property
	def duration(self):
		return self.__duration
		
		
		
		
		
		
		
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
		
		
		
		
		
	def generate_trajectory(self, state, controls_sequence):
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
						
				state = MachineState([x, y, orientation])
				
				
				yield trajectory_time, state
				