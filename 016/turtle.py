# 21/02/2024
# Day - 016

# https://docs.python.org/3/library/turtle.html

##################################################
print("\n\n*** Turtle ***")



import another_module
print(f"another_module.another_variable: {another_module.another_variable}")



import turtle
timmy = turtle.Turtle()

print(f"Timmy memory address: {timmy}")

timmy.shape("triangle")
timmy.color("DarkRed")

timmy.forward(200)
timmy.speed(1)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(50)
timmy.left(90)
timmy.forward(150)
timmy.right(90)
timmy.forward(350)



from turtle import Turtle, Screen
tommy = Turtle()

print(f"Tommy memory address: {tommy}")

tommy.shape("turtle")
tommy.color("coral")
tommy.forward(-100)



my_screen = Screen()
print(my_screen.canvheight)
# so it doesn't disappear
my_screen.exitonclick()