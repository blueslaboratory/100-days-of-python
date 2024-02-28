# 28/02/2024
# Day - 024



##################################################
print("\n\n*** Files ***")

file = open(".\\024\\my_file.txt")

contents = file.read()
print(contents)

file.close()



print("\nAnother way to open a file:")

# mode="r" --> read only mode (default)
# mode="w" --> writes in the file: deletes previous content; if the file doesn't exist, it creates it
# mode="a" --> appends in the file: does not delete previous content

with open(".\\024\\my_file_w.txt", mode="w") as file:
    file.write("New Text.")
    # closes automatically

with open(".\\024\\my_file.txt", mode="a") as file:
    file.write("\nNew Text.")
    # closes automatically

with open(".\\024\\my_file.txt") as file:
    contents = file.read()
    print(contents)
    # closes automatically
    


print("\nOpen a file from the desktop: Absolute Path")

username = "" # --> Windows Username
with open(f"\\Users\\{username}\\Desktop\\info.txt") as file:
    contents = file.read()
    print(contents)
    # closes automatically
    
    

print("\nOpen a file from the desktop: Relative Path")
# current directory = C:\Users\{username}\Desktop\100 days of python\

with open(f"..\\info.txt") as file:
    contents = file.read()
    print(contents)
    # closes automatically