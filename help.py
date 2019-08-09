side_separator = '||||'
card_separator = '\\\\\\\\'
file_path = '/Users/matt/desktop/flashcards/test123.txt'
flag_dict = {'-e': '', 'showall': 'In edit mode, shows all available cards front + back and corresponding card number'}

help_text = f"""
=== HELP ===

This app is designed to create Quizlet-ready text files which can be copy + pasted
into the 'Import Set' menu using the preset separators defined in this application.

SETTINGS:

    Path of saved .txt files...     ...{file_path}
    Flip card separator...          ...{side_separator}
    New card separator...           ...{card_separator}

COMMANDS:

These commands can be used during "Edit Mode" to perform additional actions

    showall...         ...{flag_dict['showall']}

=================

"""
help_dict = {'main': help_text, 'commands': 'special commands go here'}