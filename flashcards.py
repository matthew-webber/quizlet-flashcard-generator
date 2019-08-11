from typing import Dict, Match
import re
import help


def lower_and_strip(input):
    return input.strip().lower()


def parse_user_input(uinput):

    match_object = re.match(r"([\w\W\d]+?) (-?[e?])", uinput)
    if match_object is None:
        return uinput
    return match_object


# def create_back():
#     print("Enter back of card -- enter ^D to continue.")
#     return input()
#
#
# def create_front():
#     print("Enter front of card -- enter ^D to continue.")
#     return input()

# TEST TEST TEST TEST FUNCTIONS

def create_back(x):

    return x


def create_front(x):

    return x

###############


def show_card(picked_card):
    if picked_card:
        print(f"Front:\t{picked_card.front}")
        print(f"Back:\t{picked_card.back}")


class ModeBuilder:

    start_strings = {
        'edit': f"""
Choose which card you want to edit by typing [card_index_number_here] -e""",
        'start': f"""
What do you want to do?.

Commands: 'i' (make cards), 'e' (edit cards), 'q' (save + quit), 'x' (quit w/o saving), 'help'""",
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
            # insertion={'name': 'insertion', 'command': 'I', 'action': 'Show help file text'},
        )

    modes: Dict[str, dict] = \
        dict(
            end={'input': 'x', 'name': 'end', 'value': 0, 'startString': start_strings['end']},
            start={'input': 's', 'name': 'start', 'value': 1, 'startString': start_strings['start']},
            edit={'input': 'e', 'name': 'edit', 'value': 2, 'startString': start_strings['edit']},
            insertion={'input': 'i', 'name': 'insertion', 'value': 10, 'startString': start_strings['insertion']}
        )

    def __init__(self):
        self.mode = ModeBuilder.modes['start']

    @property
    def mode_greeting(self):
        return ModeBuilder.modes[self.mode['name']]['startString']

    def set_mode(self, mode):
        """
        Print the mode_greeting and set self.mode

        """
        self.mode = ModeBuilder.modes[mode]
        self.mode_change()

    def mode_change(self):
        print(f"*~*~* Entering {self.mode['name'].upper()} mode *~*~*")
        print(self.mode_greeting)

    def get_mode(self):
        return self.mode

    def input_to_name(self, input):
        for contents in self.modes.values():
            if input in contents.values():
                return contents['name']


class Card:

    def __init__(self, deck, index=0):
        # todo change these back to no arguments
        self.front = create_front('x')
        self.back = create_back('y')
        self.deck = deck
        self.index = self.update_index()

    def update_index(self):
        return len(self.deck.stack)  # card not yet added so index = length of parent deck's stack

    def edit_card(self, front, back):
        self.front = front
        self.back = back
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
        self.stack = stack

    def get_card(self, index):
        try:
            card = self.stack[index - 1]
        except IndexError:
            return None

        return card

    def get_deck(self):
        # todo add more properties of the deck to this dict
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

    def remove_last_card(self):
        self.stack.remove(self.stack[-1])

    def save_deck(self, deck_str):
        with open(help.file_path, 'w') as f:
            f.write(deck_str)


x = ModeBuilder()
deck = Deck()
deck.add_card()
deck.add_card()
print(x.mode_greeting)

# user prompted to select mode
mode_selection = x.input_to_name(lower_and_strip(input()))

x.set_mode(mode_selection)

# todo add text about typing quit to insertion greeting
if x.mode['name'] == 'insertion':
    while True:
        deck.add_card()

        if lower_and_strip(deck.stack[-1].front) == 'q' and lower_and_strip(deck.stack[-1].back) == 'q':
            deck.remove_last_card()
            print('Removing "quit" card...')
            print('Deck created!')
            x.set_mode('start')
            break

if x.mode['name'] == 'edit':

    while True:
        # clean and parse input
        clean_input = lower_and_strip(input())
        parsed_input = parse_user_input(clean_input)

        # if parsed input is a regex match, proceed with editing
        if isinstance(parsed_input, Match):
            card_index = int(parsed_input.group(1))
            flag = parsed_input.group(2)

            card_to_edit = deck.get_card(card_index)
            show_card(card_to_edit)
            card_to_edit.edit_card(input('\nFront:\n'), input('Back:\n'))

        # if parsed input is a command, do command action
        elif isinstance(parsed_input, str) and parsed_input in x.commands:
            print('ok')
            continue

        else:
            print('Command not recognized.')
            continue


# yyz = ModeBuilder()
# a = []

# thisthat = Card('front', 'back', 1, yyz)
#
# xya = Deck()
# xya.add_card()
# xya.add_card()
# picked_card = xya.get_card(1)
# show_card(picked_card)