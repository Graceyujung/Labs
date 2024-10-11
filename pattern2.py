import turtle

s= turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

#drawing code
#draw the first square
draw_square(200)


# move to the starting point of the second square
t.penup()
t.goto(100,-41)
t.pendown()
t.left(45)
for i in range(3):
    t.forward(200)
    t.left(90)
t.forward(200)

s.exitonclick()
