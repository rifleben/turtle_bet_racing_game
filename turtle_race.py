import random
import turtle as t

race_on = False

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will with the race? Enter a color: ")

colors = ["red", "green", "blue", "purple", "orange", "pink"]
y_positions = [-100, -70, -40, -10, 20, 50]
turtle_list = []

for index in range(0, 6):
    racer = t.Turtle(shape="turtle")
    racer.color(colors[index])
    racer.penup()
    racer.goto(x=- 225, y=y_positions[index] + 10)
    turtle_list.append(racer)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You won! {winning_color.upper()} is the winner!")
            else:
                print(f"You've lost. {winning_color} won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()