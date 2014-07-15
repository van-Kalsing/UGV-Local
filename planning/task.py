class Task:
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__machine = None
		
		self.__initial_machine_state          = None
		self.__target_machine_state           = None
		self.__target_machine_state_tolerance = None
		
		
		
		
		
	@property
	def machine(self):
		return self.__machine
		
		
	@machine.setter
	def machine(self, machine):
		self.__machine = machine
		
		
		
		
		
	@property
	def initial_machine_state(self):
		return self.__initial_machine_state
		
		
	@initial_machine_state.setter
	def initial_machine_state(self, initial_machine_state):
		self.__initial_machine_state = initial_machine_state
		
		
		
	@property
	def target_machine_state(self):
		return self.__target_machine_state
		
		
	@target_machine_state.setter
	def target_machine_state(self, target_machine_state):
		self.__target_machine_state = target_machine_state
		
		
		
	@property
	def target_machine_state_tolerance(self):
		return self.__target_machine_state_tolerance
		
		
	@target_machine_state_tolerance.setter
	def target_machine_state_tolerance(self, target_machine_state_tolerance):
		self.__target_machine_state_tolerance = target_machine_state_tolerance
		
		
		
		
		
	@property
	def machine_controls_velocities(self):
		return [-1.0, 1.0]
		# return [0.1 + a / 10 for a in range(10)] + [- 0.1 - a / 10 for a in range(10)]
		
		
		
	@property
	def machine_controls_angles(self):
		import math #!!!!!
		return [- 20.0 / 180.0 * math.pi, 0.0, 20.0 / 180.0 * math.pi]
		# return [- math.pi / 2 + (a / 10 * math.pi / 2) for a in range(11)] #!!!!!
		
		
		
	@property
	def machine_controls_durations(self):
		return [5.0, 0.125]
		# return [0.1 + a / 10 for a in range(10)] #!!!!!
		