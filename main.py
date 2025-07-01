# import colorgram
#
# colors = colorgram.extract('image.jpg', 9)
# first_color = colors[0]
# rgb = first_color.rgb
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new = (r, g, b)
#     rgb_colors.append(new)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5)]

#10 x 10 rows of spots
#dots 20 in size and 50 paces apart

leo = Turtle()
leo.hideturtle()

y_spot = -250

for i in range(10):
    y_spot += 50
    leo.teleport(-225,y_spot)
    for i in range(10):
        leo.dot(20, random.choice(color_list))
        leo.penup()
        leo.forward(50)

screen.exitonclick()
