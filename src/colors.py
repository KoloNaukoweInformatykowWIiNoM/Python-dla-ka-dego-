import turtle

bob = turtle.Turtle()

bob.pencolor("lime")
for i in range(20):
    bob.forward(50)
    bob.left(150)


bob.pencolor("blue")
for i in range(20):
    bob.forward(100)
    bob.left(150)
    
turtle.done()
