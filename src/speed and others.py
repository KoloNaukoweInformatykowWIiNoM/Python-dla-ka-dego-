import turtle

reaper = turtle.Turtle()

reaper.speed(100)

reaper.pencolor("red")

for i in range(180):
    reaper.forward(100)
    reaper.right(30)
    reaper.forward(20)
    reaper.left(60)
    reaper.forward(50)
    reaper.right(30)
    
    reaper.penup()
    reaper.setposition(0, 0)
    reaper.pendown()
    
    reaper.right(2)
    
turtle.done()
