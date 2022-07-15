import turtle
from colour_palette_extractor import color_list
import random
turtle.colormode(255)
turtle_obj = turtle.Turtle()
turtle_obj.penup()

turtle_obj.setheading(225)
turtle_obj.forward(300)
turtle_obj.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    turtle_obj.dot(20, random.choice(color_list))
    turtle_obj.forward(50)

    if dot_count % 10 == 0:
        turtle_obj.setheading(90)
        turtle_obj.forward(50)
        turtle_obj.setheading(180)
        turtle_obj.forward(500)
        turtle_obj.setheading(0)













screen = turtle.Screen()
screen.exitonclick()