import sys







def prepare_parser():
	import argparse
	
	
	
	parser = \
		argparse.ArgumentParser(
			description = \
				"Визуализация траектории наземного беспилотного транспортного\
					средства (роботизированной платформы)"
		)
		
	required_arguments = parser.add_argument_group("required arguments")
	
	
	
	parser.add_argument(
		"-c", "--control",
		type    = argparse.FileType("r"),
		default = sys.stdin,
		metavar = ("path"),
		help    = \
			"Имя файла, содержащего последовательность управляющих сигналов.\
				В случае отсутствия опции, чтение карты производится из\
				стандартного потока ввода"
	)
	
	
	required_arguments.add_argument(
		"-s", "--start",
		nargs    = 3,
		type     = float,
		required = True,
		metavar  = ("x", "y", "alpha"),
		help     = "Координаты исходного положения платформы"
	)
	
	
	required_arguments.add_argument(
		"-o", "--output",
		type     = argparse.FileType("w"),
		required = True,
		metavar  = ("path"),
		help     = \
			"Имя файла, в который производится запись визуализации траектории"
	)
	
	
	
	return parser
	
	
	
	
	
def visualize(arguments):
	from machine.config_reader       import load_machine
	from machine.machine             import MachineState, MachineControl
	from visualization.config_reader import load_visualizer
	
	import os
	
	
	
	# Создание объекта аппарата и визуализатора траектории
	script_file_name = os.path.abspath(__file__)
	directory_name   = os.path.dirname(script_file_name)
	
	
	try:
		machine_config_file = open(directory_name + "/machine.conf", "r")
		machine             = load_machine(machine_config_file)
		machine_config_file.close()
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	try:
		visualizer_config_file = open(directory_name + "/visualizer.conf", "r")
		visualizer             = load_visualizer(visualizer_config_file)
		visualizer_config_file.close()
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
		
	# Визуализация траектории аппарата
	def generate_controls_sequence():
		for control_record in arguments.control:
			velocity, angle, duration = control_record.split()
			
			control = \
				MachineControl(
					float(velocity),
					float(angle),
					float(duration)
				)
				
				
			yield control
			
			
	initial_state     = MachineState(arguments.start)
	controls_sequence = generate_controls_sequence()
	
	
	try:
		visualizer.visualize(
			machine,
			initial_state,
			controls_sequence,
			arguments.output
		)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
		
		
		
if __name__ == "__main__":
	parser    = prepare_parser()
	arguments = parser.parse_args()
	
	
	try:
		visualize(arguments)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		