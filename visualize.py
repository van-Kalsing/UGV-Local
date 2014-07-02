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
		"-t", "--time-interval",
		type     = float,
		required = True,
		metavar  = ("time-interval"),
		help     = "Интервал времени между фиксациями положений платформы"
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
	from machine.machine import Machine, MachineState, MachineControl
	from svgwrite        import Drawing, rgb
	from svgwrite.shapes import Rect, Circle
	
	import math
	
	
	
	
	
	trajectory_view_width  = 500
	trajectory_view_height = 500
	trajectory_view        = \
		Drawing(
			size = (trajectory_view_width, trajectory_view_height)
		)
		
		
	machine_state_view_width  = 30
	machine_state_view_height = 50
	
	
	
	machine = \
		Machine(
			length    = 1,
			state     = MachineState(arguments.start),
			time_step = 0.1
		)
		
	last_time = 0.0
	
	
	def draw_machine_state():
		nonlocal last_time
		
		
		need_drawing = \
			machine.time - last_time > arguments.time_interval \
				or last_time == 0.0
				
		if need_drawing:
			machine_state_view_center = \
				(int(machine.state.coordinates[0]), \
					trajectory_view_height - int(machine.state.coordinates[1]))
				
			machine_state_view_position = \
				int(machine.state.coordinates[0]) - machine_state_view_width / 2.0, \
					trajectory_view_height - (int(machine.state.coordinates[1]) + machine_state_view_height / 2.0)
					
					
			machine_state_view = \
				Rect(
					insert       = machine_state_view_position,
					size         = (30, 50),
					fill         = "#FFFFFF",
					stroke       = "#000000",
					stroke_width = 1
				)
			machine_state_view.rotate(
				- (machine.state.coordinates[2] / math.pi * 180) - 90,
				center = machine_state_view_center
			)
			
			trajectory_view.add(machine_state_view)
			
			# trajectory_view.add(
			# 	Circle(
			# 		center = machine_state_view_center,
			# 		r      = 3
			# 	)
			# )
			
			last_time += arguments.time_interval
			
			
	draw_machine_state()
	
	
	for control_record in arguments.control:
		velocity, angle, duration = control_record.split()
		velocity, angle, duration = \
			float(velocity), \
				float(angle), \
				float(duration)
				
		machine.move(
			MachineControl(velocity, angle, duration),
			draw_machine_state
		)
		
		
		
	trajectory_view.write(arguments.output)
	
	
	
	
	
if __name__ == "__main__":
	parser    = prepare_parser()
	arguments = parser.parse_args()
	
	visualize(arguments)
	