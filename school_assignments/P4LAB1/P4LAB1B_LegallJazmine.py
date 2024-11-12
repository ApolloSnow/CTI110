#importing turtle library 
import turtle

# Jazmine Legall
# 10/30/2024
# P4LAB1B
# Creating 'J' and 'L'

# Initialize Screen
wind = turtle.Screen()
wind.bgcolor('#2D293B') # Setting a background color : Gunmetal color(colors found on pinterest)


# Function for the First initial [ J ]
def draw_J(j): 
    j.penup()
    j.goto(-240, 0)
    j.pendown()
# Starting the [ J ]
    j.right(90)
    j.forward(60)
    j.circle(-20, 189)
    

# Write the letter [ J ]
turtle_J = turtle.Turtle()
turtle_J.color('#753130') # Garent color
turtle_J.pensize(3)




# Function for the Second initial [ L ]
def draw_L(l):
    l.penup()
    l.goto(10, -30)
    l.pendown()
    l.left(90)
    l.forward(60)
    l.backward(60)
    l.right(90)
    l.forward(40)

# Write the letter [ L ]
turtle_L = turtle.Turtle()
turtle_L.color('#753130') # Garent color
turtle_L.pensize(3)

# Extra way
# j.write('J', font=('monospace', 24, 'bold')) 
# L.write('L', font=('monospace', 24, 'bold'))

# Calling Function
# First initial [ J ]
draw_J(turtle_J)
turtle_J.hideturtle() # Hides the turtle(arrow)

# Second initial [ L ]
draw_L(turtle_L)
turtle_L.hideturtle() # Hides the turtle(arrow)


wind.mainloop()