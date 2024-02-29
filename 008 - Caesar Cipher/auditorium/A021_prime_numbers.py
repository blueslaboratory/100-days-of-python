# 09/02/2024
# Day - 008



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 8 - Lesson 21 - Prime Numbers
# Info: https://en.wikipedia.org/wiki/Prime_number


# Write your code below this line 👇
def prime_checker(number):
    is_prime = True

    for i in range(2, int(number/2)):
        if number % i == 0:
            is_prime = False
    
    if is_prime == True:
        print("It's a prime number.")
    else: 
        print("It's not a prime number.")
# Write your code above this line 👆


#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)