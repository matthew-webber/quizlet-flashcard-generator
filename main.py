from func import create_cards, edit_cards
import sys

list_of_cards = []
main_menu = 'M'

print('====== FLASHCARD GENERATOR ======')

while True:

    main_menu = main_menu.strip().upper()  # clean input from a re-run of loop

    if main_menu == 'M':  # root menu

        print(
            """Welcome to the main menu.
Enter 'I' to enter card insertion mode, 'Q' to quit and save or 'X' to quit w/o saving."""
        )
        main_menu = input()
        main_menu = main_menu.strip().upper()  # clean input

    if main_menu == 'Q' and list_of_cards:  # quit, cards >= 1
        print('Creating cards...')
        create_cards(list_of_cards)
        print(f'Created {len(list_of_cards)} cards!')
        print('Exiting...')
        break

    elif main_menu == 'Q':  # quit, no cards
        print('No cards to create.')
        print('Exiting...')
        break

    elif main_menu == 'X':  # quit without saving
        print('Exiting...')
        break

    elif main_menu == 'I':  # enter insertion mode
        print('***INSERTION MODE***')

    else:  # return to main menu
        print('Command not recognized.')
        main_menu = 'M'
        continue

    card = {}

    print("Enter front of card -- enter ^D to continue.")
    card_front = sys.stdin.read()

    print("Enter back of card -- enter ^D to continue.")
    card_back = sys.stdin.read()

    card[card_front] = card_back

    list_of_cards.append(card)

    print("Press Enter to add another card.  'E' to edit cards, 'Q' to quit and save, or 'X' to quit w/o saving.")

    while True:

        insertion_menu = input()

        if insertion_menu == 'E':
            print('***END INSERTION MODE***')
            list_of_cards = edit_cards(list_of_cards)
            print('Returning to main menu...')
            main_menu = 'M'

        elif insertion_menu == '':
            insertion_menu = 'I'

        main_menu = insertion_menu
        break
