from svgwrite        import Drawing, rgb
from svgwrite.shapes import Rect

import configparser
import math







class Visualizer:
	def __init__(self, machine_size, time_interval, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		
		self.__machine_length, self.__machine_width = machine_size
		self.__machine_size                         = machine_size
		self.__time_interval                        = time_interval
		
		
		
		
		
	@property
	def machine_size(self):
		return self.__machine_size
		
		
		
	@property
	def time_interval(self):
		return self.__time_interval
		
		
		
		
		
	def visualize(self, trajectory, output_file):
		drawing = Drawing()
		
		
		
		# Определение параметров образов состояний аппарата
		machine_diameter = \
			(self.__machine_width ** 2.0 + self.__machine_length ** 2.0) \
				** 0.5
				
		machine_radius = machine_diameter / 2.0
		
		
		
		# Создание последовательности записываемых состояний аппарата
		def generate_states_sequence():
			spawn_time = 0.0
			
			for trajectory_time, state in trajectory:
				if trajectory_time >= spawn_time:
					spawn_time += self.__time_interval
					
					yield state
					
					
		states_sequence = generate_states_sequence()
		
		
		
		# Запись последовательности состояний аппарата
		is_view_box_initialized                = False
		view_box_minimal_x, view_box_minimal_y = 0.0, 0.0
		view_box_maximal_x, view_box_maximal_y = 0.0, 0.0
		
		
		for state in states_sequence:
			# Создание образа состояния аппарата
			state_view_angle    = - state.coordinates[2] / math.pi * 180.0
			state_view_center   = state.coordinates[0], - state.coordinates[1]
			state_view_position = \
				state_view_center[0] - self.__machine_length / 2.0, \
					state_view_center[1] - self.__machine_width / 2.0
					
			state_view = \
				Rect(
					insert       = state_view_position,
					size         = self.__machine_size,
					fill         = rgb(255, 255, 255),
					stroke       = rgb(0, 0, 0),
					stroke_width = 1
				)
				
			state_view.rotate(
				state_view_angle,
				center = state_view_center
			)
			
			
			# Добавление образа состояния аппарата к образу траектории
			drawing.add(state_view)
			
			if is_view_box_initialized:
				view_box_minimal_x, view_box_minimal_y = \
					min(state_view_center[0], view_box_minimal_x), \
						min(state_view_center[1], view_box_minimal_y)
						
				view_box_maximal_x, view_box_maximal_y = \
					max(state_view_center[0], view_box_maximal_x), \
						max(state_view_center[1], view_box_maximal_y)
			else:
				is_view_box_initialized = True
				
				view_box_minimal_x, view_box_minimal_y = \
					state_view_center[0], \
						state_view_center[1]
						
				view_box_maximal_x, view_box_maximal_y = \
					state_view_center[0], \
						state_view_center[1]
						
						
						
		# Настройка отображения образа траектории
		drawing.viewbox(
			minx   = view_box_minimal_x - machine_radius,
			miny   = view_box_minimal_y - machine_radius,
			width  = view_box_maximal_x - view_box_minimal_x + machine_diameter,
			height = view_box_maximal_y - view_box_minimal_y + machine_diameter
		)
		
		
		
		# Запись образа траектории в файл
		try:
			drawing.write(output_file)
		except:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
			
			
			
			
			
def load_visualizer(config_file):
	def create_visualizer(parser):
		try:
			machine_length = parser.getfloat("DEFAULT", "MachineLength")
			machine_width  = parser.getfloat("DEFAULT", "MachineWidth")
			time_interval  = parser.getfloat("DEFAULT", "TimeInterval")
		except:
			raise Exception() #!!!!! Генерировать хорошие исключения
			
			
		visualizer = \
			Visualizer(
				machine_size  = (machine_length, machine_width),
				time_interval = time_interval
			)
			
		return visualizer
		
		
		
	parser = configparser.ConfigParser()
	
	
	try:
		parser.read_file(config_file)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	try:
		visualizer = create_visualizer(parser)
	except:
		raise Exception() #!!!!! Генерировать хорошие исключения
		
		
	return visualizer
	