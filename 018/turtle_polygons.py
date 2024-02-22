# 22/02/2024
# Day - 018

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

# Refactor: higlight the variable + F2




# Exercise: draw a triangle, square, pentagon, hexagon, heptagon,
#           octagon, nonagon and decagon

##################################################
print("\n\n*** Playing with the turtle: polygons ***")



from turtle import Turtle, Screen
import random



def random_rgb():
    return random.randint(0,255)


def draw_polygon(sides):
    
    # random color
    tim.color(random_rgb(), random_rgb(), random_rgb())
    
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)



screen = Screen()
tim = Turtle()


# so that random_rgb() works
screen.colormode(255)


tim.shape("turtle")
tim.speed(9)
tim.pensize(5)


# drawing the polygon:
for num_sides in range(3, 11):
    draw_polygon(num_sides)
    


screen.exitonclick()