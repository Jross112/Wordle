def game_instructions():
    print("""Wordle is a single player game
A player has to guess a five letter hidden word
You have six attempts
Your Progress Guide "✔❌❌✔➕"
"✔" Indicates that the letter at that position was guessed correctly
"➕" indicates that the letter at that position is in the hidden word, but in a different position
"❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)
    
game_instructions()

def check_word():
    hidden_word = "march"
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("you guessed the word correctly!")
            break
        else:
            attempt = attempt - 1
            print(f"you have {attempt} attempt(s)")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + " ✔")
                elif word in hidden_word:
                    print(word + " ➕")
                else:
                    print(word + " ❌")
            if attempt == 0:
                print(" Game over ! ")

check_word()