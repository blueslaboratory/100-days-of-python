# 01/03/2024
# Day - 027



##################################################
print("\n\n*** Arguments ***")



# Default values
print("\nDefault values")

def my_default_values_function(a, b=2, c=3):
    print(a, b, c)
    
my_default_values_function(5)



# Same goes for Turtle module
"""
import turtle

tim = turtle.Turtle()
tim.write("Some Text", font=("Times New Roman", 14, "normal"))

turtle.Screen().exitonclick()
"""



# Unlimited ARGumentS 
print("\nUnlimited arguments")

def add(*args):
    
    print("*args is a tuple:", args, "-", type(args))
    print(args[0])
    
    total = 0
    
    for n in args:
        total+=n
    
    return total

print(add(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))



# **kwargs: many Keyworded ARGumentS
print("\nUnlimited keyworded arguments")

def calculate(n, **kwargs):
    print("**kwargs is a dictionary:", kwargs, "-", type(kwargs))
    print(kwargs)
    
    # for key in kwargs:
    #     print(key, "-", kwargs[key])
    
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    
    print("kwargs['add']:", kwargs["add"])
    
    n += kwargs["add"]
    n *= kwargs["multiply"]
    
    print(n)

calculate(2, add=3, multiply=5)



# Car Class wit **kwargs
print("\nCar Class wit **kwargs")
class Car:
    
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        
        # But model doesn't exist so we use get:
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
    
my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)