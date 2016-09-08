#Josh Dickey 9/7/16
#this program draws four octagons that are separated by space

import turtle
#function to create octagon
def makeAOctagon():
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)

#function to move where octagons are drawn
def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#allows octagons to be filled rather than outlined
turtle.begin_fill()
#octagon color
turtle.color("red")
makeAOctagon()
turtle.end_fill()
move(-300,100)

#process repeats three more times below to create four octagons
turtle.begin_fill()
turtle.color("black")
makeAOctagon()
turtle.end_fill()
move(-400,-300)

turtle.begin_fill()
turtle.color("blue")
makeAOctagon()
turtle.end_fill()
move(277,-189)

turtle.begin_fill()
turtle.color("yellow")
makeAOctagon()
turtle.end_fill()

#makes sure that the program doesn't immediately disappear when it ends
turtle.exitonclick()
