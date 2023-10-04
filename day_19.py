from turtle import Turtle, Screen
import random

# tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

# # w = move_forward
# # s = backward
# # a = couterclockwise or leftward
# # d = clockwise or rightward
# # c = clear drawing

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtl will win the race? Enter a color: ")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "blue", "green", "red"]

y_positions = [-70, -40, -10, 20, 50, 80]

is_race_on = False

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()












