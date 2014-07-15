from planning.searching.tree_searchers.BF_searcher import BFSearcher
from planning.state                                import State







def plan(task):
	initial_state = State(task, task.initial_machine_state)
	searcher      = BFSearcher(initial_state)
	
	
	states_sequence = searcher.final_states_sequence
	
	if states_sequence is not None:
		machine_controls_sequence = []
		
		
		last_state = states_sequence[0]
		
		for state in states_sequence[1:]:
			machine_control = last_state.get_machine_control(state)
			machine_controls_sequence.append(machine_control)
			
			last_state = state
	else:
		machine_controls_sequence = None
		
		
	return machine_controls_sequence
	