from func import create_cards, list_of_cards
import sys

list_of_cards = []

while True:

    card = {}

    print("Enter front of card -- type ^D to continue.")
    card_front = sys.stdin.read()

    print("Enter back of card -- type ^D to continue.")
    card_back = sys.stdin.read()

    card[card_front] = card_back

    list_of_cards.append(card)

    print("Press enter to add another card.  Q = quit, E = edit")

    if input() != 'Q':
        continue
    elif input() == 'Q':
        create_cards(list_of_cards)
        break
    elif input() == 'E':
        edit_cards(list_of_cards)