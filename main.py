import Deck
import Player

def main():
    deck = Deck.Deck()

    # player cards
    card1 = deck.get_card()
    card2 = deck.get_card()

    player = Player.Player(card1, card2)
    print(card1)
    print(card2)
    sumOfPlayer = sum(card.get_number() for card in player.get_lst())
    print(f"sum of player is: {sumOfPlayer}")
    print()

    # dealer cards
    card3 = deck.get_card()
    card4 = deck.get_card()
    dealer = Player.Dealer(card3, card4)
    print(f"dealer's hand is {card4.__str__()}")


    while player.get_money() > 0:
        if sum(card.get_number() for card in player.get_lst()) <= 21:
            call = input("Hit or Stand ? ")
            if call == "hit":
                tmpCard = deck.get_card()
                player.add_card(tmpCard)
                print(f"sum of player is: {sum(card.get_number() for card in player.get_lst())}")

            else:
                print(f"dealer's hand is {card3.__str__()}")
                print(f"dealer's hand is {card4.__str__()}")
                sumOfDealer = sum(card.get_number() for card in dealer.get_lst())
                print(f"sum of dealer is: {sumOfDealer}")
                print()
                while sumOfDealer < 17:
                    tmpCard = deck.get_card()
                    dealer.add_card(tmpCard)
                    sumOfDealer += tmpCard.get_number()

                    print(f"dealer's hand is: {tmpCard}")
                    print(f"sum of dealer is: {sumOfDealer}")

                if sumOfDealer < sumOfPlayer or sumOfDealer > 21:
                    print("YOU ARE THE CHAMPION !!!!!")
                    break

                else:
                    print("LOSER, GAME ENDED")
                    break



        else:
            print("LOSER, GAME ENDED")
            break


if __name__ == '__main__':
    main()
