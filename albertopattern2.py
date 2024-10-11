import turtle

s= turtle.Screen()
t= turtle.Turtle()
t.shape("turtle")

#Albertomethod

t.penup()
t.forward(100)
t.left(90)
t.pendown()
t.forward(100)
t.left(90)
for i in range(4):
    t.forward(200)
    t.left(90)
t.forward(100)
t.right(90)

# second move

t.penup()
t.forward(41.42)
t.left(135)
t.pendown()
for i in range(4):
    t.forward(200)
    t.left(90)


s.exitonclick()