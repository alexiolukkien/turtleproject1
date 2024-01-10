import turtle
import random


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the turtle")
FONT= ('Arial',30,'normal')
grid_size = 10
turtle_list = []
score =0
score_turtle = turtle.Turtle()
countdown_turtle=turtle.Turtle()
game_over=False
#score turtle
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.penup()
    top_height = screen.window_height() /2
    y=top_height *0.9
    score_turtle.setpos(0,y)

    score_turtle.color("dark blue")
    score_turtle.write(arg="score:0",move=False,align="center",font=FONT)
#setup turtle
def make_turtle(x,y):
    t=turtle.Turtle()
    def handle_click(x,y):
        #print(x,y)
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(arg=f"score:{score}",move=False,align="center",font=FONT)
    t.onclick(lambda x_coord,y_coord ,t=t:handle_click(x_coord,y_coord))
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown (time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() /2
    y=top_height *0.8
    countdown_turtle.setpos(0,y)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.color("black")
        countdown_turtle.write(arg=f"Time:{time}",move=False,align="center",font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        countdown_turtle.clear()
        game_over=True
        countdown_turtle.write(arg="Game Over ! ", move=False, align="center", font=FONT)


def star_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(20)
    turtle.tracer(1)

star_game_up()
turtle.mainloop()