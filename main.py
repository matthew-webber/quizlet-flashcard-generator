from func import create_cards, edit_cards
from flashcards import Deck, Card
import sys
import help

#todo add a feature to 'open' an existing flashcard to add to it

deck = Deck()
main_menu = 'M'

print('====== FLASHCARD GENERATOR ======')

while True:

    main_menu = main_menu.strip().upper()  # clean input from a re-run of loop

    if main_menu == 'M':  # root menu

        print(
            """Welcome to the main menu.
Enter 'I' to enter card insertion mode, 'Q' to quit and save or 'X' to quit w/o saving.
Enter 'help' for more."""
        )
        main_menu = input()
        main_menu = main_menu.strip().upper()  # clean input

    if main_menu == 'Q' and deck.stack:  # quit, cards >= 1
        print('Creating cards...')
        create_cards(deck, help.file_path)
        print(f'Created {len(deck.stack)} cards!')
        print('Exiting...')
        break

    elif main_menu == 'HELP':
        print(help.help_dict['main'])
        main_menu = 'M'
        continue

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

    deck.append(card)

    print("Press Enter to add another card.  'E' to edit cards, 'Q' to quit and save, or 'X' to quit w/o saving.")

    while True:

        insertion_menu = input()
        insertion_menu = insertion_menu.strip().upper()

        if insertion_menu == 'E':
            print('***END INSERTION MODE***')
            #todo the below doesn't work
            deck.update_stack() = edit_cards(deck)
            print('Returning to main menu...')
            main_menu = 'M'
            break

        elif insertion_menu == '':
            insertion_menu = 'I'

        elif insertion_menu == 'X':
            pass

        elif insertion_menu == 'HELP':
            pass

        else:
            print('Command not recognized.')
            continue

        main_menu = insertion_menu
        break
