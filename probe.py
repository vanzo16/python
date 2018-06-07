import simple_draw as sd
from random import randint

sd.resolution = (1200, 800)



def branche(start_point, angle, length, delta_angle=30):
	if length < 10:
		return
	width = 4
	color = sd.COLOR_YELLOW
	if length < 40:
		width = 1
		color = sd.COLOR_GREEN
	elif length < 100:
		width = 2
	vector = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
	vector.draw(color=color)

	start_point_2 = vector.end_point
	angle_2 = angle - (delta_angle + randint(20, 30))
	length_2 = length * (randint(60, 90) / 100)
	branche(start_point=start_point_2, angle=angle_2, length=length_2, delta_angle=delta_angle)
	angle_3 = angle + (delta_angle + randint(20, 30))
	length_3 = length * (randint(60, 90) / 100)
	branche(start_point=start_point_2, angle=angle_3, length=length_3, delta_angle=delta_angle)

start_point = sd.get_point(x=600, y=5)
angle = 90
length = 200

branche(start_point=start_point, angle=angle, length=length, delta_angle=00)
branche(start_point=start_point, angle=angle, length=length, delta_angle=10)
branche(start_point=start_point, angle=angle, length=length, delta_angle=20)
branche(start_point=start_point, angle=angle, length=length, delta_angle=30)
branche(start_point=start_point, angle=angle, length=length, delta_angle=40)




sd.pause()
