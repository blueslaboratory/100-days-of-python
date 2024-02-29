# 20/02/2024
# Day - 015



##################################################
# DAY 15 PROJECT: Coffee Machine: my solution

print("\n*** Welcome to the Coffee Machine ☕ ***")

from PJ_data import art, MENU, resources, resources_units
import os

machine_on = True
profit = 0


def machine_report():
    """returns machine current report status"""
    global profit
    
    print("\n---- Machine Status Report ----")
    
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}{resources_units[item]}")
        
    print(f"Profit: ${profit}")
    print("-------------------------------")


def check_ingredients(ingredients):
    """checks if there are sufficient ingredients"""
    for key in ingredients:
        if(ingredients[key] > resources[key]):
            print(f"\nSorry, there is not enough {key}")
            print(f"- Available: {resources[key]}{resources_units[key]}")
            print(f"- Needed: {ingredients[key]}{resources_units[key]}")
            return False
        
    return True
    

def process_coins():
    """this is where the machine process the coins"""
    dolars = int(input("\nHow many $1 bills: "))
    quarters = int(input("How many $0.25 coins: "))
    dimes = int(input("How many $0.10 coins: "))
    nickles = int(input("How many $0.05 coins: "))
    pennies =  int(input("How many $0.01 coins: "))
    
    total_input_coins = 1*dolars + 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    return round(total_input_coins, 2)


def check_transaction(user_order, user_coins):
    """checks if the transaction has been successful"""
    global profit
    price = user_order["cost"]
    
    print(f"\nPrice: ${price}")
    print(f"You introduced: ${user_coins}")
    
    if user_coins >= price:
        change = round(user_coins - price, 2)
        print(f"Your change is: ${change}")
        profit += price
        return True
    else:
        print(f"Sorry, ${user_coins}, is not enough money. Money refunded.")
        return False


def update_resources(ingredients):
    """updates the machine resources"""
    for key in ingredients:
        resources[key] -= ingredients[key]


def replenish():
    """replenishes in +300 units each of the resources"""
    for item in resources:
        resources[item] += 300
        

print(art)


while machine_on:
    option = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if option == "off":
        machine_on = False
    elif option == "report":
        machine_report()
    elif option in MENU:
        order_ingredients = MENU[option]["ingredients"]
        
        if check_ingredients(order_ingredients):
            input_coins = process_coins()
            
            if check_transaction(MENU[option], input_coins):
                update_resources(order_ingredients)
                
                print(f"\nYour {option} ☕ is ready! Please enjoy!")
    elif option == "replenish":
        replenish()
    elif option == "clear":
        os.system("cls")
        print(art)
    else:
        print("Please introduce a valid option: espresso/latte/cappuccino")