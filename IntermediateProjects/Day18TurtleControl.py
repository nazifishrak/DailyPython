import turtle

turtle_obj = turtle.Turtle()
screen = turtle.Screen()
def move_forward():
    turtle_obj.forward(50)
def turn_left():
    turtle_obj.left(10)
def turn_right():
    turtle_obj.right(10)
def move_backwards():
    turtle_obj.backward(50)
def clear():
    turtle_obj.clear()
    turtle_obj.home()
screen.listen()
screen.onkey(key = "w", fun= move_forward)
screen.onkey(key = "d", fun= turn_right)
screen.onkey(key = "a", fun= turn_left)
screen.onkey(key = "s", fun= move_backwards)
screen.onkey(key = "c", fun= clear)




screen.exitonclick()