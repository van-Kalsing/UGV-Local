from svgwrite        import Drawing, rgb
from svgwrite.shapes import Circle, Line





first_circle_center, first_circle_radius   = (100.0, 157.0), 77.0
second_circle_center, second_circle_radius = (270.0, 353.0), 53.5

drawing_file_name = "/home/van_kalsing/Desktop/tmp.svg"
drawing_size      = 500, 500





def draw():
	drawing = Drawing(drawing_file_name, drawing_size)
	
	
	first_circle_view = \
		Circle(
			center       = first_circle_center,
			r            = first_circle_radius,
			fill_opacity = 0,
			stroke       = rgb(0, 0, 0),
			stroke_width = 1
		)
		
	first_circle_center_view = \
		Circle(
			center       = first_circle_center,
			r            = 3,
			fill         = rgb(0, 0, 0),
			stroke_width = 0
		)
		
	drawing.add(first_circle_view)
	drawing.add(first_circle_center_view)
	
	
	second_circle_view = \
		Circle(
			center       = second_circle_center,
			r            = second_circle_radius,
			fill_opacity = 0,
			stroke       = rgb(0, 0, 0),
			stroke_width = 1
		)
		
	second_circle_center_view = \
		Circle(
			center       = second_circle_center,
			r            = 3,
			fill         = rgb(0, 0, 0),
			stroke_width = 0
		)
		
	drawing.add(second_circle_view)
	drawing.add(second_circle_center_view)
	
	
	drawing.save()
	
	
	
	
	
if __name__ == "__main__":
	draw()
	