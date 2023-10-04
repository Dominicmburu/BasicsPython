import turtle as t
import random

tim = t.Turtle()
tim.shape("arrow")
tim.speed("fastest")

t.colormode(255)

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "blue", "green", "red", "cyan", "magenta", "wheat", "green", "slateGray", "DeepSkyBlue", "SeaGreen"]

## coding 1

# def draw_shape(num_sides):

#     angle = 360 / num_sides

#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_sides in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shape_sides)

## coding 2

# direction = [0, 90, 180, 270]
# tim.pensize(15)

# def random_color():
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     color = (red, green, blue)
#     return color


# for _ in range(300):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

## coding 3

# def draw_a_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         current_heading = tim.heading()
#         tim.setheading(current_heading + size_of_gap)

# draw_a_spirograph(1)

## coding 4
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r  
    g = color.rgb.g 
    b = color.rgb.b
    new_color = (r,g,b) 
    rgb_colors.append(new_color)

t.colormode(255)
tim = turtle_module.Turtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.penup()
tim.hideturtle()

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()