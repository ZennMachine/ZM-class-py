import random

J = 11
Q = 12
K = 13

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]


def get_new_card():
    card = random.randrange(0, 12)
    return card


def compare_card(old_card, new_card):
    if old_card > new_card:
        return True
    else:
        return False


def game_run():
    is_wrong = False
    score = 0
    while not is_wrong:
        old_card = get_new_card()
        print(get_new_card(), "Is the next card higher or lower?")
        user_in = input("h or l? ")
        new_card = get_new_card()
        is_higher = compare_card(old_card, new_card)
        if user_in == "h" and is_higher:
            print(new_card)
            print("Correct")
            score += 1
            print(score)
        elif user_in == "h" and not is_higher:
            print(new_card)
            is_wrong = True
        elif user_in == "l" and not is_higher:
            print(new_card)
            print("Correct")
            score += 1
        else:
            print(new_card)
            is_wrong = True
        # Replace the old card with the new card
        old_card = new_card
    print("Game Over")


if __name__ == '__main__':
    game_run()
