from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["CornflowerBlue", "SpringGreen", "RosyBrown", "OliveDrab", "SlateGray", "DarkOrchid"]

starting_point = -70

for color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=starting_point)
    tim.color(color)
    starting_point += 30

screen.exitonclick()