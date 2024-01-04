class Player:
    def __init__(self, card1, card2):
        self.__money = 5000
        self.__lst = [card1, card2]


    def update_money(self, money):
        self.__money += money

    def get_money(self):
        return self.__money

    def get_lst(self):
        return self.__lst

    def add_card(self, card):
        self.__lst.append(card)


class Dealer:
    def __init__(self, card1, card2):
        self.__lst = [card1, card2]

    def get_lst(self):
        return self.__lst

    def add_card(self, card):
        self.__lst.append(card)