import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.color("red")
t.speed(8)

for i in range(10):
    for i in range(5):
        t.forward(100)
        t.right(72)
    t.right(36)

t.color("blue")
t.left(72)

for i in range(10):
    for i in range(10):
        t.forward(50)
        t.right(36)
    t.right(36)



s.exitonclick()