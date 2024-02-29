# 22/02/2024
# Day - 018

# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors
# https://trinket.io/docs/colors

# Refactor: higlight the variable + F2



# https://en.wikipedia.org/wiki/Random_walk
# Exercise: draw a random walk, each time it turns: random color;
#           turns can only be 90º, increase the thickness of the pen

##################################################
print("\n\n*** Playing with the turtle: random walk ***")



from turtle import Turtle, Screen
import random



def random_rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    # tuples are immutable
    color_tuple = (r, g, b)
    
    return color_tuple


def random_line():
    
    # random color
    tim.color(random_rgb())
    
    directions = [0, 90, 180, 270]
    rand_direction = random.choice(directions)
    
    tim.setheading(rand_direction)
    tim.forward(20)
    



screen = Screen()
tim = Turtle()


# so that random_rgb() works
screen.colormode(255)


tim.shape("turtle")
tim.speed(10)
tim.pensize(10)


# drawing the line:
for i in range(150):
    random_line()
    


screen.exitonclick()