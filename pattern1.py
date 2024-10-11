# draw some patterns
# 'turtle package' (turtle.py)
import turtle

# I need to know how to use this package.
# "Read the documentation (manual)"

# 1. create a window
# variable - named storage
screen = turtle.Screen()

# a = 10

# 2. create a turtle (brush)
t = turtle.Turtle()
# turtle_brush = turtle.Turtle()
t.shape("turtle")
t.color("blue")

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

# draw a blue square
draw_square(100)

t.penup()
t.goto(-20,-20)
t.pendown()

# second square
draw_square(140)



# python
# 1. variable name should start with a lowercase letter


screen.exitonclick()

