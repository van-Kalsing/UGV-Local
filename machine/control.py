class Control:
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
		