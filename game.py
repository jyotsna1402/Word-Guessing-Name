import random

def play_round(word_list, round_num):
    word = random.choice(word_list).lower()
    attempts = 5
    round_score = 0
    print(f"\n🔹 Round {round_num} - Guess the word ({len(word)} letters)!")
    
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        
        if not guess.isalpha():
            print("❌ Invalid input! Enter a word with letters only.")
            continue
        
        if guess == word:
            round_score = attempts * 10
            print(f"🎉 Correct! The word was '{word}'. You scored {round_score} points this round!")
            return round_score
        
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")
    
    print(f"😢 Out of attempts! The word was '{word}'.")
    return round_score

def main():
    word_rounds = [
        ["cat", "dog", "hat", "sun"],
        ["fish", "tree", "bird", "moon"],
        ["apple", "house", "chair", "beach"],
        ["planet", "rocket", "guitar", "garden"],
        ["sudoku", "skibidi", "puzzle", "sigma"]
    ]
    
    total_score = 0
    print("\n🎮 Welcome to the Word Guessing Game! Five rounds, increasing difficulty! 🎮")
    
    for round_num, words in enumerate(word_rounds, start=1):
        total_score += play_round(words, round_num)
    
    print(f"\n🏆 Game Over! Your Total Score: {total_score} points!")
    
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            main()
        elif play_again == "no":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()