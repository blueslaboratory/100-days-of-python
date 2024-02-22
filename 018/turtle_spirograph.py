# 22/02/2024
# Day - 018

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

# Refactor: higlight the variable + F2



# https://en.wikipedia.org/wiki/Random_walk
# Exercise: draw a spirograph

##################################################
print("\n\n*** Playing with the turtle: spirograph ***")



from turtle import Turtle, Screen
import random



def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    # tuples are immutable
    color_tuple = (r, g, b)
    
    return color_tuple


def random_circle(tilt):
    
    # random color
    tim.color(random_rgb())

    tim.right(360/tilt)
    tim.circle(100)
    


screen = Screen()
tim = Turtle()

# so that random_rgb() works
screen.colormode(255)

tim.shape("turtle")
tim.speed(0)

# drawing the spirograph:
n_circles = 100
for i in range(n_circles):
    random_circle(n_circles)
    

screen.exitonclick()