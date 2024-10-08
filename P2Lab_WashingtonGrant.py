# Grant Washington
# 10/06/24
# P2LAb
# write code that performs mathematical calculations and displays information to users

import math

radius=float(input("What is the radius of the circle? " ))
diameter=radius*2
print("The diameter of the circle is ", end='')
print(f'{diameter:.1f}')
circumference=2*math.pi*radius
print("The cirumference of the circle is ", end='')
print(f'{circumference:.2f}')
area=math.pi*radius**2
print("The area of the circle is ", end='')
print(f'{area:.3f}')