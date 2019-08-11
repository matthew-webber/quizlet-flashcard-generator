from typing import Dict
import help


def create_back():
    print("Enter back of card -- enter ^D to continue.")
    return input()


def create_front():
    print("Enter front of card -- enter ^D to continue.")
    return input()


class ModeBuilder:

    start_strings = {
        'edit': f"""
Choose which card you want to edit by typing [card_index_number_here] -e""",
        'start': f"""
Welcome to the main menu.

Commands: 'I' (make cards), 'Q' (save + quit), 'X' (quit w/o saving), 'help'""",
        'end': """""",
        'insertion': """""",
    }

    commands = \
        dict(
            #todo parse out showall to be show + all
            quit={'name': 'quit', 'command': 'Q', 'action': 'Exit current mode'},
            save={'name': 'save', 'command': 'S', 'action': 'Save the current file/deck'},
            showall={'name': 'showall', 'command': 'showall', 'action': 'Show all files/cards/decks/etc.'},
            help={'name': 'help', 'command': 'help', 'action': 'Show help file text'},
            insertion={'name': 'insertion', 'command': 'I', 'action': 'Show help file text'},
        )

    modes: Dict[str, dict] = \
        dict(
            end={'name': 'end', 'value': 0, 'startString': start_strings['end']},
            start={'name': 'start', 'value': 1, 'startString': start_strings['start']},
            edit={'name': 'edit', 'value': 2, 'startString': start_strings['edit']},
            insertion={'name': 'insertion', 'value': 10, 'startString': start_strings['insertion']}
        )

    def __init__(self):
        self.mode = ModeBuilder.modes['start']

    @property
    def mode_greeting(self):
        return ModeBuilder.modes[self.mode['name']]['startString']

    def mode_change(self):
        print(f"*~*~* Entering {self.mode['name'].upper()} mode *~*~*")
        print(self.mode_greeting)

    def set_mode(self, mode):
        """
        Print the mode_greeting and set self.mode

        """
        self.mode = ModeBuilder.modes[mode]
        self.mode_change()

    def get_mode(self):
        return self.mode


class Card:

    def __init__(self, index=0, deck=''):
        self.front = create_front()
        self.back = create_back()
        self.index = index
        self.deck = deck

    def update_index(self):
        self.index = self.deck

    # def open_card(self):
    #
    #     card_num = int(self.index) - 1  # decrement index to offset 'starts at zero'
    #     edited_card = list_of_cards[card_num]
    #     try:
    #         for front, back in edited_card.items():
    #             print('Front:\t' + front)
    #             print('Back:\t' + back)
    #             new_front = front
    #             new_back = back
    #     except IndexError:
    #         print('Error: Card index does not exist.')
    #         return 0
    #     pass


class Deck:

    def __init__(self, stack=[]):
        assert isinstance(stack, list)
        self.stack = stack

    def get_deck(self):
        return {'length': len(self.stack)}

    # def update_stack(self, stack):
    #     for card in stack:
    #         self.stack.append(card)

    def refresh_deck(self):
        self.stack = []
        return

    def create_deck_string(self):

        deck_str = help.card_separator

        for card in self.stack:
            for front, back in card.items():
                deck_str = deck_str + str(front) + help.side_separator + str(back) + help.card_separator

        return deck_str

    def add_card(self):
        new_card = Card(deck=self)
        self.stack.append(new_card)

    def save_deck(self, deck_str):

        with open(help.file_path, 'w') as f:
            f.write(deck_str)


yyz = ModeBuilder()
a = []

# thisthat = Card('front', 'back', 1, yyz)
xya = Deck()
xya.add_card()
