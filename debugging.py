# debugging shit sheet

letters_guessed = ['a', 'b', 'c']

guess = input("Guess a letter: ").lower()

if guess in letters_guessed:
    print(f"\nLetter '{guess}' has already been guessed")
else:
    letters_guessed.append(guess)
    print(letters_guessed)