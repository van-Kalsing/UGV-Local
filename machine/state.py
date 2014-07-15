class State:
	def __init__(self, coordinates, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__coordinates = tuple(coordinates)
		
		
		
	@property
	def coordinates(self):
		return self.__coordinates
		
		
		
		
		
		
		
def compute_states_distance(first_state, second_state):
	delta_x = \
		abs(
			first_state.coordinates[0] \
				- second_state.coordinates[0]
		)
		
	delta_y = \
		abs(
			first_state.coordinates[1] \
				- second_state.coordinates[1]
		)
		
	distance = \
		(delta_x ** 2.0 + delta_y ** 2.0) \
			** 0.5
			
			
	return distance
	
	
	
	
	
	
	
class StateTolerance:
	def __init__(self, bounds, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__bounds = tuple(bounds)
		
		
		
	def check_equivalence(self, first_state, second_state):
		coordinates = \
			zip(
				first_state.coordinates,
				second_state.coordinates
			)
			
		differences = \
			[abs(first_coordinate - second_coordinate) \
				for first_coordinate, second_coordinate
				in coordinates]
				
				
		are_states_equivalent = True
		
		for difference, bound in zip(differences, self.__bounds):
			are_states_equivalent &= difference <= bound
			
			
		return are_states_equivalent
		