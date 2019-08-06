from func import create_cards, create_card_file
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

    print("Press enter to add another card.  Type quit to quit.")

    if input() != 'quit':
        continue
    else:
        create_cards(list_of_cards)
        break