import Deck
import Player

def main():
    deck = Deck.Deck()

    # player cards
    card1 = deck.get_card()
    if card1.get_number() == 1:
        card1.set_number(11)

    card2 = deck.get_card()
    if card1.get_number() == 11:
        card2.set_number(1)
    elif card1.get_number() == 10:
        card2.set_number(11)

    player = Player.Player(card1, card2)
    player.print_sum_of_player_and_cards()
    money = player.get_money()
    print(f"you got {money}$")
    print()

    # dealer cards
    card3 = deck.get_card()
    if card3.get_number() == 1:
        card3.set_number(11)

    card4 = deck.get_card()
    if card3.get_number() == 11:
        card4.set_number(1)
    elif card1.get_number() == 10:
        card2.set_number(11)

    dealer = Player.Dealer(card3, card4)
    print(f"dealer's hand is {card4.__str__()}")

    bet = input("place your bet: ")
    while int(bet) > money:
        bet = input("invalid bet, place valid bet: ")

    while player.get_money() > 0:
        if player.get_sum_of_player() <= 21:
            call = input("Hit or Stand ? ")
            if call == "hit":
                tmpCard = deck.get_card()
                if tmpCard.get_number() == 1:
                    if player.get_sum_of_player() + 11 < 21:
                        tmpCard.set_number(11)

                player.add_card(tmpCard)
                player.print_sum_of_player_and_cards()

            else:
                print("dealer's hand is: \n")
                dealer.print_sum_of_dealer_and_cards()
                print()

                while dealer.get_sum_of_dealer() < 17:
                    tmpCard = deck.get_card()
                    if tmpCard.get_number() == 1:
                        if dealer.get_sum_of_dealer() + 11 > 21:
                            tmpCard.set_number(1)

                    dealer.add_card(tmpCard)
                    dealer.print_sum_of_dealer_and_cards()
                    print()

                if dealer.get_sum_of_dealer() < player.get_sum_of_player() or dealer.get_sum_of_dealer() > 21:
                    print("YOU ARE THE CHAMPION !!!!!")
                    money += int(bet)
                    print(f"you got {money}$")
                    print("______________________________________ \n")
                    break

                else:
                    print("LOSER, GAME ENDED")
                    money -= int(bet)
                    print(f"you got {money}$")
                    print("______________________________________ \n")
                    break

        else:
            print("LOSER, GAME ENDED")
            print(f"you got {money}$")
            print("______________________________________ \n")
            break


    while player.get_money() > 0:
        card1 = deck.get_card()
        if card1.get_number() == 1:
            card1.set_number(11)

        card2 = deck.get_card()
        if card1.get_number() == 11:
            card2.set_number(1)
        elif card1.get_number() == 10:
            card2.set_number(11)

        card2 = deck.get_card()
        if card1.get_number() == 11:
            card2.set_number(1)
        elif card1.get_number() == 10:
            card2.set_number(11)

        player.print_sum_of_player_and_cards()

        card3 = deck.get_card()
        if card3.get_number() == 1:
            card3.set_number(11)

        card4 = deck.get_card()
        if card3.get_number() == 11:
            card4.set_number(1)
        elif card1.get_number() == 10:
            card2.set_number(11)

        dealer = Player.Dealer(card3, card4)
        print(f"dealer's hand is {card4.__str__()}")

        print(f"you got {money}$")
        bet = input("place your bet: ")
        while int(bet) > money:
            bet = input("invalid bet, place valid bet: ")

        if player.get_sum_of_player() <= 21:
            call = input("Hit or Stand ? ")
            if call == "hit":
                tmpCard = deck.get_card()
                if tmpCard.get_number() == 1:
                    if player.get_sum_of_player() + 11 < 21:
                        tmpCard.set_number(11)

                player.add_card(tmpCard)
                player.print_sum_of_player_and_cards()

            else:
                print("dealer's hand is: \n")
                dealer.print_sum_of_dealer_and_cards()
                print()

                while dealer.get_sum_of_dealer() < 17:
                    tmpCard = deck.get_card()
                    if tmpCard.get_number() == 1:
                        if dealer.get_sum_of_dealer() + 11 > 21:
                            tmpCard.set_number(1)

                    dealer.add_card(tmpCard)
                    dealer.print_sum_of_dealer_and_cards()
                    print()

                if dealer.get_sum_of_dealer() < player.get_sum_of_player() or dealer.get_sum_of_dealer() > 21:
                    print("YOU ARE THE CHAMPION !!!!!")
                    money += int(bet)
                    print("______________________________________ \n")


                else:
                    print("LOSER, GAME ENDED")
                    money -= int(bet)
                    print("______________________________________ \n")

        else:
            print("LOSER, GAME ENDED")
            print()


if __name__ == '__main__':
    main()
