import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

#drawing code
def draw_square_from_center(size):
    t.right(90)
    t.forward(size /2)
    for i in range(3):
        t.left(90)
        t.forward(size)
    t.left(90)
    t.forward(size /2)
    t.left(90)

for i in range(5):
    draw_square_from_center(200)
    t.left(72)

s.exitonclick()
