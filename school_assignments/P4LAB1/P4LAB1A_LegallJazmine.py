#importing turtle library 
import turtle

# Jazmine Legall
# 10/30/2024
# P4LAB1A
# Practice using turtle library. Creating shapes like squares and circles. 


# # Initialize Screen
wind = turtle.Screen()
# Creating a background for turtle
turtle.bgcolor('black') 
# Creating a title on the window
wind.title('Squares & Triangles')


# Creating my first shape

# Square
square = turtle.Turtle() # creating square and its attributes
square.color('salmon')
square.pensize(3)

# Make square draw a Square
# Begin Fill
square.begin_fill()

# Completes a Square with 4 sides
for _ in range(4) :
    square.forward(100)
    square.left(90)

# Fill in Square
square.end_fill()
# End of Square
square.penup()
# Move pen 
square.forward(130)
# Place pen back down
square.pendown()



# Triangle
triangle = turtle.Turtle()

# Move Triangle off of Square
triangle.backward(250)
# Triangle color
triangle.color('#06b6b4')
triangle.pensize(5)

triangle.begin_fill()
# Make triangle draw Triangle
triangle.forward(80)
triangle.left(120)
triangle.forward(80)
triangle.left(120)
triangle.forward(80)
triangle.left(120)

# Fill in
triangle.end_fill()
# End of Triangle
triangle.penup()
# Move pen 
triangle.forward(110)
# Place pen back down
triangle.pendown()





# Finish to display turtle
wind.mainloop()