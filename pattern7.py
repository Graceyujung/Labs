import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.color("blue")
s.bgcolor("light green")


#drawing code

t.stamp()
for i in range(12):
    t.penup()
    t.forward(200)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(20)
    t.stamp()
    t.goto(0, 0)
    t.left(30)


s.exitonclick()
