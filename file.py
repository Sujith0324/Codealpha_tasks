import random

def play_hangman():
    words = ["python", "coding", "developer", "algorithm", "function"]
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("\n=== HANGMAN ===")
    print(f"Guess the word! You have {max_incorrect} incorrect guesses allowed.\n")
    
    while incorrect_guesses < max_incorrect:
        # Display current state
        display = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print(f"Word: {display}")
        print(f"Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining incorrect guesses: {max_incorrect - incorrect_guesses}")
        
        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n🎉 You won! The word was '{secret_word}'")
            return
        
        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print(f"✓ '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f"✗ '{guess}' is not in the word.")
        
        print("-" * 30)
    
    print(f"\n💀 Game over! The word was '{secret_word}'")

if __name__ == "__main__":
    play_hangman()
