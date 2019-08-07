import re


def create_cards(list_of_cards, file_str=''):

    for card in list_of_cards:
        for front, back in card.items():
            file_str = file_str + front + '||||' + back + '\\\\\\\\'

    create_card_file(file_str)


def create_card_file(file_str, file_path='/Users/matt/desktop/test123.txt'):

    with open(file_path,'w') as f:
        f.write(file_str)


def edit_cards(list_of_cards):

    #
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

    print('***EDIT MODE***')

    while True:

        #  ask for user input
        print('Choose which card you want to edit.  Enter Q to exit edit mode.')
        uinput = input()

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
        except AttributeError:
            #  ...check if input is a special command, if yes, execute command, otherwise restart loop
            cmd = command.strip().lower()
            if cmd == 'help':
                #todo help display
                pass
            elif cmd == 'showall':
                #todo show action
                pass
            # elif cmd == '':
            #     #todo show all cards
            #     pass

            continue

        #  if parsing completes, check if command valid, check if flag valid, restart loop if not
        if not card_num.strip().lower().isdigit():
            print('Special commands do not take flags.  Enter a command or number and try again.')
            continue

        if flag not in flag_dict:
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

    except IndexError:
        print('Error: Card index does not exist.')
        return 0

    #  ask user to reassign card
    print('Reassign front or press Enter to skip.')
    new_front = input()
    print('Reassign back or press Enter to skip.')
    new_back = input()

    edited_card[new_front] = edited_card.pop(front)
    edited_card[new_front] = new_back

    return list_of_cards


    #  shitty rework dict key from list = list[1]['AND'] = list[1].pop('and')


def parse_user_input(uinput):

    match_object = re.match(r"([\w\W\d]+?) (-?[e?])", uinput)
    if match_object is None:
        return uinput
    return match_object
