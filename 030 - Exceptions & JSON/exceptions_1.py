# 04/03/2024
# Day - 030



##################################################
print("\n\n*** Exceptions ***")

try:
    file = open(".\\030 - Exceptions & JSON\\non_existent_file.txt")
    # if the exception is raised, the below code isn't executed:
    
    dictionary = {"key": "value"}
    # print(dictionary["non_existent_key"])

except FileNotFoundError:
    print("There was an error: FileNotFoundError")
    print("The file was created")
    
    file = open(".\\030 - Exceptions & JSON\\non_existent_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The dictionary key {error_message} doesn't exist.")

else:
    # triggered only if the exceptions aren't raised
    content = file.read()
    print(content)

finally:
    # always executed
    file.close()
    print("File was closed.")
    
    try:
        raise TypeError("made up error")
    except TypeError:
        print("he he, you thought you could escape without exceptions")