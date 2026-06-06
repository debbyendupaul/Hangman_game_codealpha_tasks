import random

WORDS = ['python', 'galaxy', 'jungle', 'bridge', 'flaunt']

GALLOWS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

MAX_WRONG = 6


def get_display(word, guessed):
    return ' '.join(letter if letter in guessed else '_' for letter in word)


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("\nWelcome to Hangman!")
    print(f"The word has {len(word)} letters.\n")

    while wrong < MAX_WRONG:
        print(GALLOWS[wrong])
        print(f"\nWord:  {get_display(word, guessed)}")

        wrong_letters = sorted(l for l in guessed if l not in word)
        print(f"Wrong: {', '.join(wrong_letters) if wrong_letters else '—'}")
        print(f"Lives: {MAX_WRONG - wrong} remaining\n")

        if all(l in guessed for l in word):
            print(f"✓ You guessed it! The word was '{word.upper()}'.")
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("! Please enter a single letter.\n")
            continue

        if guess in guessed:
            print(f"! You already tried '{guess.upper()}'.\n")
            continue

        guessed.add(guess)

        if guess in word:
            count = word.count(guess)
            print(f"+ '{guess.upper()}' is in the word! ({count}×)\n")
        else:
            wrong += 1
            print(f"- '{guess.upper()}' is not in the word.\n")

    print(GALLOWS[wrong])
    print(f"\n✗ Game over! The word was '{word.upper()}'.")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()