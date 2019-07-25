#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

class Card:
    def __init__(self, suit:str, value:str or int):
        '''Sets up card instance'''
        self.suit = suit
        self.value = value
        self.card_value = self.get_card_value()

    def get_card_value(self):
        '''Gets the value needed for blackjack'''
        if type(self.value) == int:
            return self.value
        elif self.value in ["J", "Q", "K"]:
            return 10
        else:
            return self.ace_value()

    def ace_value(self, total): #Need to fix
        '''Gets the ace value'''
        if total <= 10:
            return 11
        else:
            return 1

    def __repr__(self):
        if type(self.value) == str:
            return "Card('{}', '{}')".format(self.suit, self.value)
        else:
            return "Card('{}', {})".format(self.suit, self.value)

    def __str__(self):
        return "{} {}".format(self.suit, self.value)


