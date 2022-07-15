from turtle import Turtle, Screen, position
from random import randint
import random
import turtle
turtle_obj = Turtle()
turtle_obj.pu()
turtle_obj.goto(50,250)
turtle_obj.pd()
turtle_obj.speed(0)
turtle.colormode(255)
turtle_obj.shape("circle")
turtle_obj.color("black")

def dashed_forward(distance: int):
    for i in range(int(distance/25)):
        turtle_obj.pd()
        turtle_obj.forward(25)
        turtle_obj.pu()
        turtle_obj.forward(25)

def draw_dashed_square(size):
    
    for i in range(4):
        dashed_forward(size)
        turtle_obj.right(90)

def draw_polygon(n,length):
    """
    Draws n sided polygons starting from a triangle
    """
    side = 3
    angle = 120
    while n>3:
        turtle_obj.color((randint(50,255),randint(10,255),randint(50,255)))
        for i in range(side):
            turtle_obj.forward(length)
            turtle_obj.right(angle)
        n-=1
        side +=1
        angle = 360/side
        
def random_walk(length):
    turtle_obj.speed(6)
    turtle_obj.pensize(15)
    
    for i in range(1000):
        turtle_obj.color((randint(50,255),randint(10,255),randint(50,255)))
        turtle_obj.forward(length)
        turtle_obj.setheading(random.choice([0,90,180,270]))


def draw_spirograph(radius: int, size_of_gap):

    turtle_obj.speed(0)
    turtle_obj.pu()
    turtle_obj.goto(50,50)
    turtle_obj.pd()
    turtle_obj.pensize(2)
    for i in range(int(360/size_of_gap)):
        turtle_obj.color((randint(50,255),randint(10,255),randint(50,255)))
        turtle_obj.circle(radius)
        turtle_obj.setheading(turtle_obj.heading()+size_of_gap)


# draw_polygon(10,100)     
# random_walk(50)
# draw_spirograph(50,5)

inp = input(f"""Which drawing do you want to see:
            1. Dashed Square
            2. Overlapped Polygons
            3: Random Walk
            4: Spirograph

            Choose from 1,2,3,4: 

""")

if inp == "1":
    draw_dashed_square(int(input("what is the length:")))
elif inp =="2":
    draw_polygon(int(input("largest polygon you want to go upto:")), int(input("what is the length of side:")))
elif inp =="3":
    random_walk(int(input("what is the length of each walk: ")))
elif inp == "4":
    draw_spirograph(int(input("what is the radius:")), int(input("what is the gap between circles:")))


screen = Screen()
screen.exitonclick()