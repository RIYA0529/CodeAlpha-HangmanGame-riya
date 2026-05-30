import random

print("=================================")
print("   WELCOME TO HANGMAN GAME")
print("=================================")

word_list = ["python", "laptop", "coding", "github", "internship"]
secret_word = random.choice(word_list)

used_letters = []
attempts_left = 7

while attempts_left > 0:

    hidden_word = ""

    for ch in secret_word:
        if ch in used_letters:
            hidden_word += ch + " "
        else:
            hidden_word += "_ "

    print("\nWord :", hidden_word)
    print("Used Letters :", used_letters)
    print("Attempts Left :", attempts_left)

    if "_" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    user_letter = input("Enter a letter: ").lower()

    if user_letter in used_letters:
        print("⚠ You already entered this letter.")
        continue

    used_letters.append(user_letter)

    if user_letter in secret_word:
        print("✅ Correct Guess!")
    else:
        attempts_left -= 1
        print("❌ Wrong Guess!")

if attempts_left == 0:
    print("\n💀 Game Over!")
    print("Correct Word Was :", secret_word)