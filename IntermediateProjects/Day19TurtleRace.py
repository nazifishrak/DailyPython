from random import randint,choice
import random
import turtle

HEIGHT = 400
WIDTH = 500
screen = turtle.Screen()
screen.setup(width=500, height= 400)
user_resp = screen.textinput(title="Make your bet", prompt="Which turtle will win the race(red/pink/orange/green/blue? Enter a color: ") 
def createTurtle(color, x,y):
    name = turtle.Turtle()
    name.shape('turtle')
    name.pu()
    name.color(color)
    name.setpos(x,y)
    name.col = color
    return name

# Constructing Turtles Instances
turtle1 = createTurtle("red", -200,70)
turtle2 = createTurtle("pink", -200,30)
turtle3 = createTurtle("orange", -200,-10)
turtle4 = createTurtle("green", -200,-50)
turtle5 = createTurtle("blue", -200,-90)

list_of_turtle = [turtle1,turtle2,turtle3,turtle4,turtle5]
def finished(tur: turtle.Turtle):
    if tur.xcor() >= WIDTH/2:
        return True
    else:
        return False

def check_winner(answer: str, turtle: turtle.Turtle):
    if turtle.xcor()>=(WIDTH/2 -30):
        if str(turtle.col) == answer:
            print(f'You won, {str(turtle.col)} turtle won')  
        else:
            print(f'You lost,{turtle.col} turtle won ')      

race_not_finished =True

while race_not_finished:
    random_number = random.randint(0,len(list_of_turtle)-1)
    turt =  list_of_turtle[random_number]
    turt.forward(random.randint(0,10))
    if turt.xcor()>=(WIDTH/2 -30):
        check_winner(user_resp,turt)
        race_not_finished = False

   

screen.exitonclick()
