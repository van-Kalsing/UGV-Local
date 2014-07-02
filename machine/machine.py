import math





class MachineState:
	def __init__(self, coordinates, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__coordinates = tuple(coordinates)
		# self.__velocity    = velocity
		
		
		
	@property
	def coordinates(self):
		return self.__coordinates
		
		
	# @property
	# def velocity(self):
	# 	return self.__velocity
		
		
		
		
		
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
	def __init__(self, length, state, time_step, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__length = length
		self.__state  = state
		
		self.__time      = 0.0
		self.__time_step = time_step
		
		
		
	@property
	def length(self):
		return self.__length
		
		
	@property
	def state(self):
		return self.__state
		
		
		
	@property
	def time(self):
		return self.__time
		
		
	@property
	def time_step(self):
		return self.__time_step
		
		
		
	#!!!!! callback сделано временно, нужно будет выдавать сообщения
	def move(self, control, callback):
		velocity, angle   = control.velocity, control.angle
		x, y, orientation = self.__state.coordinates
		
		
		
		residual_time = control.duration
		
		while residual_time > 0.0:
			x += velocity * math.cos(orientation) * self.__time_step
			y += velocity * math.sin(orientation) * self.__time_step
					
			orientation += \
				velocity / self.__length * math.tan(angle) \
					* self.__time_step
					
					
			self.__state  = MachineState([x, y, orientation])
			self.__time  += self.__time_step
			
			callback()
			
			
			residual_time -= self.__time_step
			