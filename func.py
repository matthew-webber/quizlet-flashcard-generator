import re

flag_dict = {'-e':'', 'all':''}

def create_cards(list_of_cards, file_str=''):

    for card in list_of_cards:
        for front, back in card.items():
            file_str = file_str + front + '|otherside|' + back + '|newcard|'

    create_card_file(file_str)


def create_card_file(file_str, file_path='/Users/matt/desktop/test123.txt'):

    with open(file_path,'w') as f:
        f.write(file_str)

def edit_cards(list_of_cards):

    #  ask for user input
    #  user can enter special commands or pick card number to edit
    #
    #  EDITING
    #  card is picked by entering an integer followed by the -e flag
    #  card front/back is printed
    #  prompt x 2 for front / back
    #  print "Card changed."
    #  return to main loop

    #  SPECIAL COMMANDS
    #  "show all" = show all cards, printing a 1. , 2. , etc. by each card
    #  "show [number]" = show card corresponding to [number]

    while True:

        print('Choose which card you want to edit.')
        uinput = input()

        command = parse_user_input(uinput)

        try:
            cmd = command.group(1)
        except AttributeError:

            cmd = command.strip().lower()
            #todo if command in list of special commands, do that
            # otherwise, return to top, print "Error: Command not recognized."
            continue

        flag = command.group(2)

        if flag not in flag_dict:
            print('Error: flag not recognized.')
            continue

        try:
            list_of_cards[int(cmd)]
        except IndexError:
            print('Error: Card index does not exist.')
            continue

        open_card(list_of_cards, cmd)

def open_card(list_of_cards, card_num):

    print(list_of_cards[int(card_num)])



def parse_user_input(uinput):

    match_object = re.match(r"([\w\W\d]+?) (-?\w+)", uinput)
    if match_object is None:
        return uinput
    return match_object


a = edit_cards([1,2,3])
print('done!')