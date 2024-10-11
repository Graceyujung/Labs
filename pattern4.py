import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("pink")

#drawing code
for i in range(6):
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.left(60)


s.exitonclick()