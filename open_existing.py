'''
Working copy created in scratch file and added to project for tracking purposes.
This will be new dev copy... deleting scratch file.
'''

import os
import re

# the 'showall' for files in a folder
file_path = "/Users/matt/desktop/flashcards/"
file_list = os.listdir(file_path)

for file in file_list:
    file_index = int(file_list.index(file))
    print(f'{file_index + 1}.    {file}')


# open the file by index
print('Pick a file number.')
#uinput = int(input()) - 1
uinput = 1
chosen_file = file_list[uinput]

with open(file_path + file_list[uinput], 'r') as f:
    file_str = f.read()

card_fronts = re.findall(r'\\{4}([\w\W]+?)\|{4}', file_str)
card_backs = re.findall(r'\|{4}([\w\W]+?)\\{4}', file_str)

loc = []

x = zip(card_fronts, card_backs)

for front, back in x:
    card_dict = {front: back}
    loc.append(card_dict)

for i in loc:
    print(i)
