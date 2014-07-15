from machine.control          import Control as MachineControl
from planning.searching.state import EvaluatedState as EvaluatedSearchingState
from utilities.memoization    import memoization

from machine.state \
	import compute_states_distance as compute_machine_states_distance
	
import itertools







#!!!!! Возможно вместо копирования задачи поиска нужно реализовать ее заморозку
class State(EvaluatedSearchingState):
	def __init__(self, task, machine_state, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__task          = task
		self.__machine_state = machine_state
		
		self.__generate_successors_map = \
			memoization(
				self.__generate_successors_map
			)
			
			
			
			
			
	@property
	def task(self):
		task = self.__task.copy()
		
		return task
		
		
		
	@property
	def machine_state(self):
		return self.__machine_state
		
		
		
		
		
	@property
	def is_final(self):
		is_final = \
			self.__task.target_machine_state_tolerance \
				.check_equivalence(
					self.__task.target_machine_state,
					self.__machine_state
				)
				
				
		return is_final
		
		
		
		
		
	@property
	def estimation(self):
		distance = \
			compute_machine_states_distance(
				self.__task.target_machine_state,
				self.__machine_state
			)
			
		return distance
		
		
		
		
		
	def __generate_successors_map(self):
		def generate_trajectories():
			controls_parameters = \
				itertools.product(
					self.__task.machine_controls_velocities,
					self.__task.machine_controls_angles,
					self.__task.machine_controls_durations
				)
				
			for control_parameters in controls_parameters:
				control           = MachineControl(*control_parameters)
				controls_sequence = [control]
				
				trajectory = \
					self.__task.machine \
						.compute_trajectory(
							self.__machine_state,
							controls_sequence
						)
						
				yield trajectory, control
				
				
				
		def generate_successors(trajectories):
			def generate_successor(trajectory, control):
				successor     = None
				transfer_cost = 0.0
				
				for _, machine_state in trajectory:
					if successor is not None:
						transfer_cost += \
							compute_machine_states_distance(
								successor.machine_state,
								machine_state
							)
							
					successor = State(self.__task, machine_state)
					
					
					is_final_state = \
						self.__task.target_machine_state_tolerance \
							.check_equivalence(
								self.__task.target_machine_state,
								machine_state
							)
							
					if is_final_state:
						break
						
						
				successor_record = \
					{
						"transfer_cost":   transfer_cost,
						"machine_control": control
					}
					
					
				return successor, successor_record
				
				
			for trajectory, control in trajectories:
				successor, successor_record = \
					generate_successor(
						trajectory,
						control
					)
					
				yield successor, successor_record
				
				
				
		trajectories   = generate_trajectories()
		successors     = generate_successors(trajectories)
		successors_map = dict(successors)
		
		return successors_map
		
		
		
	@property
	def successors(self):
		successors_map = self.__generate_successors_map()
		
		successors = successors_map.keys()
		successors = list(successors)
		
		return successors
		
		
		
	def get_transfer_cost(self, successor):
		successors_map = self.__generate_successors_map()
		
		if successor in successors_map:
			successor_record = successors_map[successor]
			transfer_cost    = successor_record["transfer_cost"]
		else:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		return transfer_cost
		
		
		
	def get_machine_control(self, successor):
		successors_map = self.__generate_successors_map()
		
		if successor in successors_map:
			successor_record = successors_map[successor]
			machine_control  = successor_record["machine_control"]
		else:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		return machine_control
		