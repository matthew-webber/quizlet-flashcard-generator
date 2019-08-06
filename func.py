def create_cards(list_of_cards, file_str=''):

    for card in list_of_cards:
        for front, back in card.items():
            file_str = file_str + front + '|otherside|' + back + '|newcard|'

    create_card_file(file_str)


def create_card_file(file_str, file_path='/Users/matt/desktop/test123.txt'):

    with open(file_path,'w') as f:
        f.write(file_str)

def edit_cards(list_of_cards):

    #  ask for user input, user can enter special commands or pick card number to edit
    #  show all cards, printing a 1. , 2. , etc. by each card
    #