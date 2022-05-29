import random


def computer_cards(list_of_cards):
    computer_deck = []
    for i in range(10):
        computer_deck.append(random.choice(list_of_cards))
    return computer_deck

def who_wins(player, computer):
    if player > computer:
        print("You win this round!")
        return True
    else:
        print("You lose this round!")
        return False

def player_cards(list_of_cards):
    player_deck = []
    for i in range(10):
        player_deck.append(random.choice(list_of_cards))
    return player_deck


def main():
    list_of_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
                     10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
    player_deck = player_cards(list_of_cards)
    computer_deck = computer_cards(list_of_cards)
    print(player_deck)
    print(computer_deck)
    while True:
        player_card_played = player_deck.pop(0)
        computer_card_played = computer_deck.pop(0)
        if who_wins(player_card_played, computer_card_played):
            player_deck.append(player_card_played)
            player_deck.append(computer_card_played)
        else:
            computer_deck.append(computer_card_played)
            computer_deck.append(player_card_played)
        if computer_deck == []:
            print("You Win the game!")
            break
        if player_deck == []:
            print("You lost the game!")
            break
main()