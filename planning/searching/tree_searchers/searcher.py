from utilities.memoization import memoization

import abc







#!!!!! Ввести для записей специальный класс, вместо словарей
class Searcher(metaclass = abc.ABCMeta):
	def __init__(self, initial_state, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__initial_state = initial_state
		
		self.__search = memoization(self.__search)
		
		
		
		
		
	@property
	def initial_state(self):
		return self.__initial_state
		
		
		
		
		
	@abc.abstractproperty
	def _contains_perspective_states_records(self):
		pass
		
		
		
	@abc.abstractmethod
	def _insert_perspective_state_record(self, perspective_state_record):
		pass
		
		
		
	@abc.abstractmethod
	def _retrieve_perspective_state_record(self):
		pass
		
		
		
		
		
	def __search(self):
		initial_state_record = \
			{
				"state":       self.__initial_state,
				"predecessor": None,
				"cost":        0.0
			}
			
		self._insert_perspective_state_record(initial_state_record)
		
		
		
		while self._contains_perspective_states_records:
			state_record = self._retrieve_perspective_state_record()
			state        = state_record["state"]
			cost         = state_record["cost"]
			
			
			# print(state.machine_state.coordinates)
			if state.is_final:
				final_states_sequence = []
				
				while state_record is not None:
					final_states_sequence.insert(0, state_record["state"])
					
					state_record = state_record["predecessor"]
					
				break
				
				
			else:
				for successor_state in state.successors:
					transfer_cost = state.get_transfer_cost(successor_state)
					
					
					successor_state_record = \
						{
							"state":       successor_state,
							"predecessor": state_record,
							"cost":        cost + transfer_cost
						}
						
					self._insert_perspective_state_record(
						successor_state_record
					)
		else:
			final_states_sequence = None
			
			
			
		return final_states_sequence
		
		
		
	@property
	def final_states_sequence(self):
		final_states_sequence = self.__search()
		
		if final_states_sequence is not None:
			final_states_sequence = list(final_states_sequence)
			
			
		return final_states_sequence
		