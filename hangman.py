import random

def computer_draw():
    list_of_words = ["charmander", "squirtle", "bulbasaur", "regelieki", "sudowoodo"]
    computer_choice = random.choice(list_of_words)
    return computer_choice

def player_letter_input():
    player_choice = input("Select a letter: ")
    return player_choice

def word_cover(word):
    covered_word = ""
    for i in word:
        i = "-"
        covered_word += i
    return covered_word

def word_guessing(word,player_word):
    if word == player_word:
        return True
    else:
        return False

def

def main_game(word, player, cover):
    temp_word = list(cover)
    for i, v in enumerate(word):
        if v == player:
            temp_word[i] = v
    return temp_word



def hangman():
    print("""Welcome to the hangman game.
Your task is to set free a poor man from stretching his neck, by guessing the word that i think of.
Fortunately you will see the length of the word. Just type the letter this word contains and voila!
Another man can enjoy their free life. But watch out your bad guesses are limited to 5.
If u cant guess the word in that time the man will hung, and u will be partially a executioner.
So go, free some people. (or go on killing spree (-: )""")
    tries = 5
    killed_people = 0
    saved_people = 0
    while True:
        computer_choice = computer_draw()
        word_covered = word_cover(computer_choice)
        print(f"\nThe word that i think of is \n {word_covered}")
        while tries >= 1:
            print(f"Tries left {tries}")
            player_choice = input("Guess the letter --> ")
            temporary_word = main_game(computer_choice, player_choice, word_covered)
            if temporary_word == list(word_covered):
                print("Opps! You missed.")
                tries -= 1
            else:
                print("Bingo! good job.")
            player_guess_word = input("Would you like to guess the word? [Y/N]")
            player_guess_word = player_guess_word.casefold()
            if player_guess_word == "y":
                player_guess = input("Guess the word: ")
                if word_guessing(computer_choice,player_guess):
                    print("You saved a life!!!")
                    break
                else:
                    print("Thats not the word!")
                    tries -= 1
            if temporary_word == list(computer_choice):
                print("You saved a life!!!")
                break
            word_covered = temporary_word
        if tries < 1:
            print("This poor man died because of you.")
            killed_people += 1
        else:
            saved_people += 1
        continuation = input("Would you like to continue? [Y/N] --> ")
        continuation = continuation.lower()
        continuation = continuation[0]
        if continuation == "n":
            break


hangman()