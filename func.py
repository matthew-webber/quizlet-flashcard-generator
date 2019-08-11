import re
import help

#
# def create_cards(list_of_cards, file_path, file_str=r'\\\\'):
#
#     for card in list_of_cards:
#         for front, back in card.items():
#             file_str = file_str + front + help.side_separator + back + help.card_separator
#             print(file_str)
#
#     create_card_file(file_str, file_path)

#
# def create_card_file(file_str, file_path='/Users/matt/desktop/test123.txt'):
#
#     with open(file_path,'w') as f:
#         f.write(file_str)

def upper_and_strip(input):

    return input.strip().upper()

def edit_cards(list_of_cards):

    print('***EDIT MODE***')

    while True:

        #  ask for user input
        print('Choose which card you want to edit.  Enter Q to exit edit mode.')
        uinput = input().strip().upper()

        #  exit edit mode
        if uinput.strip().upper() == 'Q':
            print('***END EDIT MODE***')
            return list_of_cards

        #  parse input
        command = parse_user_input(uinput)

        try:
            card_num = command.group(1)
            flag = command.group(2)
        #  if parsing does not complete successfully (i.e. more or less than a command + flag is entered)...
        #  ...check if input is a special command, if yes, execute command, otherwise restart loop
        except AttributeError:
            cmd = command.strip().lower()

            if cmd == 'help':
                print(help.help_dict['main'])
                continue

            elif cmd == 'showall':
                for card in list_of_cards:
                    i = list_of_cards.index(card) + 1
                    for front, back in card.items():
                        print(f"""Card #{i} {front}/{back}""")

            continue

        #  if parsing completes, check if command valid, check if flag valid, restart loop if not
        if not card_num.strip().lower().isdigit():
            print('Special commands do not take flags.  Enter a command or number and try again.')
            continue

        if flag not in help.flag_dict:
            print('Error: flag not recognized.')
            continue

        list_of_cards = open_card(list_of_cards, card_num)


def open_card(list_of_cards, card_num):

    card_num = int(card_num) - 1  # decrement index to offset 'starts at zero'
    edited_card = list_of_cards[card_num]
    try:
        for front, back in edited_card.items():
            print('Front:\t' + front)
            print('Back:\t' + back)
            new_front = front
            new_back = back



    #  ask user to reassign card
    print('Reassign front or press Enter to skip.')

    if input().strip() != '':
        new_front = input()

    print('Reassign back or press Enter to skip.')

    if input().strip() != '':
        new_back = input()

    edited_card[new_front] = edited_card.pop(front)
    edited_card[new_front] = new_back

    return list_of_cards


def parse_user_input(uinput):

    match_object = re.match(r"([\w\W\d]+?) (-?[e?])", uinput)
    if match_object is None:
        return uinput
    return match_object

#a = edit_cards([{"a": "b"},{"c": "d"}])