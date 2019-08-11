from flashcards import Deck, Card, ModeBuilder
import sys
import help

#todo add a feature to 'open' an existing flashcard to add to it

deck = Deck()

a = [{1:2},{3:4}]

deck.update_stack(a)
b = deck.create_deck_string()
deck.save_deck(b)

mode = ModeBuilder('edit')
mode = ModeBuilder('edit)')
# print(deck.stack)