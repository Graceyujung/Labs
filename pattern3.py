import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

#drawing code
for i in range(2):
    t.forward(100)
    t.left(90)
for i in range(3):
    t.forward(200)
    t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
for i in range(3):
    t.forward(200)
    t.left(90)

s.exitonclick()
