import random

colors = ['heart', 'diamond', 'clubs', 'spades']
class Card:
    def __init__(self, color, number):
        self.__color = color
        self.__number = number

    def get_color(self):
        return self.__color

    def get_number(self):
        return self.__number

    def __str__(self):
        return f"color: {colors[self.__color]}, number: {self.__number}"


class Deck:
    def __init__(self):
        self.__deck = {'heart': 13, 'diamond': 13, 'clubs': 13, 'spades': 13}

    def get_deck(self):
        return self.__deck


    def get_card(self):
        color = random.randint(0, 3)
        if self.__deck[colors[color]] > 0:
            maxNumOfCards = self.__deck[colors[color]]
            number = random.randint(1, maxNumOfCards)
            card = Card(color, number)
            self.__deck[colors[color]] -= 1
            return card

        else:
            color = random.randint(1, 5)