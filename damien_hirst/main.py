"""This program uses python's turtle module and the colorgram package to produce the Damien hirst painting.
The colorgram package helped in copying the colors in a .jpg picture of Hirst's painting which was downloaded
from the internet"""
import turtle
from turtle import Turtle, Screen
import random
import colorgram

turtle.colormode(255)
def extract_rgb_colors(picture, number_of_colors):
    """Uses python's colorgram package to extract a specified number of colors
    (number_of_colors) from a given picture saved in .jpg/jpeg format (picture) and returns tuple of rgb colors"""
    # import colors from the hirst picture using the extract function
    colors = colorgram.extract(picture, number_of_colors)
    all_rgb_colors = []
    for number in range(number_of_colors):
        color = colors[number]
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        new_rgb = (red, green, blue)
        all_rgb_colors.append(new_rgb)
    return all_rgb_colors

extracted_colors = extract_rgb_colors("hirstpic.jpg", 8)

# Create screen
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600, bg="Ivory")

# Create turtle
timy = Turtle()
timy.penup()
timy.setpos(-100,-100)
random_colors = [(216, 151, 109), (35, 103, 168), (156, 58, 91), (151, 82, 54), (229, 235, 52), (235,146,52),
                 (52,232,235), (235,52,174), (140, 52, 235)]

def draw_hirst(x_pos, y_pos, number_of_x_dots, number_of_y_dots, dot_thickness, dot_distance):
    x_start_point = x_pos
    y_start_point = y_pos
    timy.setpos(x_start_point,y_start_point)
    for x_dots in range(number_of_x_dots):
        for y_dots in range(number_of_y_dots):
            new_color = random.choice(random_colors)
            timy.color(new_color)
            timy.dot(dot_thickness)
            timy.forward(dot_distance)
            timy.hideturtle()
        y_start_point += dot_distance
        timy.setpos(x_start_point, y_start_point)

# Call the draw_hirst() function
draw_hirst(-250, -250, 12, 10, 20, 50)

screen.exitonclick()


