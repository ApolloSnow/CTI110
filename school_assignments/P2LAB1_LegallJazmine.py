# Jazmine Legall
# 09/26/2024
# P2LAB1
# Creating a calc for Circle Formulas and displays output
import math 

radius = float(input("What is the radius of the circle? "))
print()
print(f"The diameter of the circle is {2 * radius:.1f}")
print()
print(f"The circumference of the circle is {round(2 * math.pi * radius, 2):.2f}")
print()
print(f"The area of the circle is {round(math.pi * radius ** 2, 3):.2f}")
