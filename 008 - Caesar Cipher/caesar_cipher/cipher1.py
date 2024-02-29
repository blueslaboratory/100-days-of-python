# 09/02/2024
# Day - 008



##################################################
# Hint: https://www.w3schools.com/python/ref_list_index.asp
print("\n\n*** Caesar Cipher 1 ***")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amount):

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards 
    # in the alphabet by the shift amount and print the encrypted text.
    
    # e.g. 
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    ## HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ## 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    text_index = []

    for letter in plain_text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            shifted_index = letter_index + shift_amount

            if shifted_index < len(alphabet):
                shifted_letter = alphabet[shifted_index]
            else:
                shifted_letter = alphabet[shifted_index - len(alphabet)]

            text_index.append(shifted_letter)

        else:
            text_index.append(letter)

    print(f"Here's the encoded result: {''.join(text_index)}")


# TODO-3: Call the encrypt function and pass in the user inputs.
# You should be able to test the code and encrypt a message. 
encrypt(text, shift)