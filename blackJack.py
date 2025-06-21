import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def adjust_for_ace(cards):
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1

def calculate_score(cards):
    adjust_for_ace(cards)
    return sum(cards)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print(art.logo)

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 21:
            print("Blackjack! You win 😎")
            game_over = True
        elif player_score > 21:
            print("You went over 21. You lose 😭")
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_cards.append(random.choice(cards))
            else:
                while calculate_score(computer_cards) < 17:
                    computer_cards.append(random.choice(cards))
                computer_score = calculate_score(computer_cards)
                print(f"Your final hand: {player_cards}, final score: {player_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                if computer_score > 21 or player_score > computer_score:
                    print("You win 😁")
                elif player_score < computer_score:
                    print("You lose 😤")
                else:
                    print("It's a draw 😐")
                game_over = True

print("Thanks for playing!")
