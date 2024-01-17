import Deck

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

    def print_sum_of_player_and_cards(self):
        cards_Sum = 0
        for card in self.__lst:
            cards_Sum += card.get_number()
            print(card.__str__())

        print(f"sum of player is: {cards_Sum}")
        print()

    def get_sum_of_player(self):
        cards_Sum = 0
        for card in self.__lst:
            cards_Sum += card.get_number()

        return cards_Sum

class Dealer(Player):
    def __init__(self, card1, card2):
        Player.__init__(self, card1, card2)
        self.__lst = [card1, card2]

    def print_sum_of_dealer_and_cards(self):
        cards_Sum = 0
        for card in self.__lst:
            cards_Sum += card.get_number()
            print(card.__str__())

        print(f"sum of dealer is: {cards_Sum}")
        print()

    def get_sum_of_dealer(self):
        cards_Sum = 0
        for card in self.__lst:
            cards_Sum += card.get_number()

        return cards_Sum

    def add_card(self, card):
        self.__lst.append(card)