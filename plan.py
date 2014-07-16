from machine.machine  import load_machine
from planning.planner import plan
from planning.task    import Task as PlanningTask

from machine.state \
	import State as MachineState, \
			StateTolerance as MachineStateTolerance
			
import math
import os







planning_task = PlanningTask()


# Создание объекта платформы
script_file_name = os.path.abspath(__file__)
directory_name   = os.path.dirname(script_file_name)

try:
	machine_config_file   = open(directory_name + "/machine.conf", "r")
	planning_task.machine = load_machine(machine_config_file)
	machine_config_file.close()
except:
	raise Exception() #!!!!! Генерировать хорошие исключения
	
	
planning_task.initial_machine_state          = MachineState([0.0, 0.0, 0.0])
planning_task.target_machine_state           = MachineState([0.0, 0.3, 0.0])
planning_task.target_machine_state_tolerance = \
	MachineStateTolerance(
		[0.1, 0.1, 0.25 * math.pi]
		# [0.05, 0.05, 0.0625 * math.pi]
	)
	
	
machine_controls_sequence = plan(planning_task)

if machine_controls_sequence is not None:
	for machine_control in machine_controls_sequence:
		print("%s %s %s" % (machine_control.velocity, machine_control.angle, machine_control.duration))
else:
	print("Нет пути")
	