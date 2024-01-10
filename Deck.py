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

    def set_number(self, number):
        self.__number = number

    def __str__(self):
        return f"color: {self.__color}, number: {self.__number}"


class Deck:
    def __init__(self):
        self.__deck = []
        for number in range(1, 14):
            if number > 10:
                number = 10

            for color in colors:
                card = Card(color, number)
                self.__deck.append(card)

        random.shuffle(self.__deck)

    def get_card(self):
        return self.__deck.pop()

    def get_first_cards(self):
        lst = (Deck.get_card(self), Deck.get_card(self))
        return lst