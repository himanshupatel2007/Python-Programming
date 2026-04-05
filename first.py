import math
arc_angle = 60
arc_radius = 42
wire_length = (arc_angle / 360) * 2 * math.pi * arc_radius
perimeter = wire_length
side = perimeter/ 4
area = side ** 2
print(f"The area of the square formed by this wire is: {area} square units.")
