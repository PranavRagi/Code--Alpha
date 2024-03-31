import random
import os

def choose_word(filename):
    # Check if the file exists
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            words = f.readlines()
        return random.choice(words).strip()  # strip() removes leading/trailing whitespaces
    else:
        print(f"Error: The file '{filename}' was not found.")
        return None

def display_word(word, guesses):
    display = ''
    for letter in word:
        if letter.lower() in guesses:
            display += letter
        else:
            display += "_"
    return display

def main():
    filename = 'words_list.txt'
    word = choose_word(filename)

    if word is None:
        return

    allowed_errors = 7
    guesses = []

    while True:
        print(display_word(word, guesses))

        if "_" not in display_word(word, guesses):
            print(f"You found the word! It was {word}!")
            break

        if allowed_errors == 0:
            print(f"Game Over! The word was {word}!")
            break

        guess = input(f"Allowed Errors left {allowed_errors}, Next Guess: ").lower()
        guesses.append(guess)

        if guess not in word.lower():
            allowed_errors -= 1

if __name__ == "__main__":
    main()
