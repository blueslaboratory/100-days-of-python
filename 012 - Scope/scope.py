# 14/02/2024
# Day - 012



##################################################
print("\n\n*** Scope ***")



# Global Scope: available anywhere from our file
enemy = "Skeleton"
player_health = 10

def increase_enemies():
    # Local Scope: namespace available only 
    # inside the function in which it is declared
    enemy = "Zombie"
    potion_strength = 2
    
    print("\nLocal Scope:")
    print(f"Enemies inside function: {enemy}")
    
    # Accessing a global variable
    print(f"Player health: {player_health}")

increase_enemies()
print("\nGlobal Scope:")
print(f"Enemies outside function: {enemy}")

# potion_strength is in local scope: can't access it
# print(potion_strength)



# There is no Block Scope in Python: the following is valid
print("\nBlock Scope:")

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[2]
    
print(new_enemy)



# Modifying a global variable
def increase_player_health():
    print("\nModifying a global variable:")
    global player_health
    player_health += 1
    print(f"New player health: {player_health}")
    # you usually don't do this but:
    # return player_health + 1

increase_player_health()



# Global scope is useful when we define: constants
PI = 3.14159
URL = "https://github.com/blueslaboratory"
INSTRUCTOR_TWITTER_HANDLE = "@yu_angela"