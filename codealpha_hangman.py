import random

def hangman():
    words = ["python", "apple", "chair", "house", "plane","man", "pen","pencil","book"]
    word = random.choice(words)

    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman Game!")
    print("You have 6 incorrect guesses.\n")

    while attempts_left > 0:
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word.strip())
        print("Guessed letters:", " ".join(guessed_letters))
        print("Attempts left:", attempts_left)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("Wrong guess!\n")
        else:
            print("Good guess!\n")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
