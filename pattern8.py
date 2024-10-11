import turtle

s = turtle.Screen()
t = turtle.Turtle()

#drawing code
# t.right(144)
# t.forward(20)
# t.right(144)
# t.forward(40)
# t.right(144)
# t.forward(60)


for i in range(20):
    t.forward(i*15)
    t.right(144)


s.exitonclick()