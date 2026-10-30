import random

words = ["apple", "python", "tiger", "chair", "hello"]

word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed this letter!")
    elif guess in word:
        guessed.append(guess)
        print("Correct guess!")
    else:
        guessed.append(guess)
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("You lost! The word was:", word)
