import Deck
import Player

def main():
    deck = Deck.Deck()

    # create cards of player and print cards
    card1_player = deck.get_card()
    if card1_player.get_number() == 1:
        card1_player.set_number(11)

    card2_player = deck.get_card()
    player = Player.Player(card1_player, card2_player)
    print(f"you got {player.get_money()}$")
    player.print_sum_of_player_and_cards()

    # create cards of dealer and print 4th card
    card3_dealer = deck.get_card()
    if card3_dealer.get_number() == 1:
        card3_dealer.set_number(11)

    card4_dealer = deck.get_card()
    dealer = Player.Dealer(card3_dealer, card4_dealer)
    print(f"dealer's hand is: {card4_dealer}")

    bet = input("place your bet: ")
    while (int(bet) > player.get_sum_of_player()) or (int(bet) < 0):
        bet = input("Invalid bet, please enter valid bet: ")

    while True:
        while player.get_sum_of_player() <= 21:
            call = input("Hit or Stand: \n")
            if call == "hit":
                tmp_card = deck.get_card()
                if tmp_card.get_number() == 1 and player.get_sum_of_player() + 11 < 21:
                    tmp_card.set_number(11)

                player.add_card(tmp_card)
                player.print_sum_of_player_and_cards()
                if player.get_sum_of_player() > 21:
                    print("LOSER, YOU LOST")
                    print(f"you got {player.get_money()}$")
                    break

            else:
                dealer.print_sum_of_dealer_and_cards()
                print()
                while dealer.get_sum_of_dealer() < 17:
                    tmp_card = deck.get_card()
                    if dealer.get_sum_of_dealer() + 11 < 21:
                        tmp_card.set_number(11)

                    dealer.add_card(tmp_card)

                dealer.print_sum_of_dealer_and_cards()
                break

        if player.get_sum_of_player() > 21 or (dealer.get_sum_of_dealer() >= player.get_sum_of_player() and dealer.get_sum_of_dealer() <= 21):
            print("LOSER, YOU LOST")
            print(f"you got {player.get_money()}$")
            break

        else:
            print("YAY YOU WON !!!!!")
            player.update_money(int(bet) * 2)
            print(f"you got {player.get_money()}$")
            break








if __name__ == '__main__':
    main()
