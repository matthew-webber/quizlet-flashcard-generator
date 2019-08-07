from func import create_cards, edit_cards
import sys

list_of_cards = []

print('***FLASHCARD GENERATOR***')

while True:

    print(
"""Welcome to the main menu.
Enter 'I' to enter card insertion mode, 'Q' to quit and save or 'X' to quit w/o saving."""
    )

    main_menu = input()
    main_menu = main_menu.strip().upper()  # clean input

    # if asked to quit and cards >= 1

    if main_menu == 'Q' and list_of_cards:
        print('Creating cards...')
        #create_cards(list_of_cards)
        print(f'Created {len(list_of_cards)} cards!')
        print('Exiting...')
        break

    elif main_menu == 'Q':  # if asked to quit and cards = 0
        print('No cards to create.')
        print('Exiting...')
        break

    # quit without saving

    elif main_menu == 'X':
        print('Exiting...')
        break

    # enter insertion mode

    elif main_menu == 'I':
        print('***INSERTION MODE***')

    # unrecognized command

    else:
        print('Command not recognized.')

    card = {}

    print("Enter front of card -- enter ^D to continue.")
    card_front = sys.stdin.read()

    print("Enter back of card -- enter ^D to continue.")
    card_back = sys.stdin.read()

    card[card_front] = card_back

    list_of_cards.append(card)

    print("Press Enter to add another card.  'E' to edit cards, 'Q' to quit and save, or 'X' to quit w/o saving.")

    if main_menu == 'E':
        edit_cards(list_of_cards)


