# 21/02/2024
# Day - 017

# PascalCase: class names
# snake_case: everything else



##################################################
print("\n\n*** Class User ***")

class User:
    
    def __init__(self, user_id, username):
        
        # called everytime an object is created
        print("Called everytime an object is created")
        
        # attributes
        self.id = user_id
        self.username = username
        
        # attributes with default value
        self.followers = 0
        self.following = 0
        
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        


# mandatory: when we create an object User, 
# 2 parameters must be passed: id & username
# user_0 = User() --> will give an error

user_1 = User("001", "angela")
user_2 = User("002", "jack")

print(user_1.id, user_1.username)


user_1.follow(user_2)
print(f"\nuser_1.followers: {user_1.followers}, user_1.following: {user_1.following}")
print(f"user_2.followers: {user_2.followers}, user_2.following: {user_2.following}")