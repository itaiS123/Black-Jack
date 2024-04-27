import Deck
import Player

def deal_cards(deck):
    card1 = deck.get_card()
    if card1.get_number() == 1:
        card1.set_number(11)

    card2 = deck.get_card()
    arr = [card1, card2]

    return arr

def place_bet(player):
    bet = input("Place your bet: ")
    while int(bet) < 0 or int(bet) > player.get_money():
        bet = input("Place your bet: ")

    return int(bet)

def run_game(deck, player, dealer):
    while player.get_sum_of_player() <= 21:
        call = input("hit or stand: ")
        if call == "hit":
            tmp_card = deck.get_card()
            if tmp_card.get_number() == 1 and player.get_sum_of_player() + 11 < 21:
                tmp_card.set_number(11)
            player.add_card(tmp_card)

            player.print_sum_of_player_and_cards()

            if player.get_sum_of_player() > 21:
                return False

        else:
            print()
            while dealer.get_sum_of_dealer() < 17:
                tmp_card = deck.get_card()
                if tmp_card.get_number() == 1 and dealer.get_sum_of_dealer() + 11 < 21:
                    tmp_card.set_number(11)
                dealer.add_card(tmp_card)

            dealer.print_sum_of_dealer_and_cards()
            if dealer.get_sum_of_player() > 21:
                return True
            break



    if player.get_sum_of_player() < dealer.get_sum_of_dealer() or player.get_sum_of_player() == dealer.get_sum_of_dealer():
        return False

    return True


def main():
    deck = Deck.Deck()
    arr = deal_cards(deck)

    card1 = arr[0]
    card2 = arr[1]
    player = Player.Player(card1, card2)
    player.print_sum_of_player_and_cards()

    # change

    arr = deal_cards(deck)
    card3 = arr[0]
    card4 = arr[1]
    dealer = Player.Dealer(card3, card4)
    print(f"dealer's hand is: {card2.__str__()} \n")



    print(f"You have {player.get_money()}$")
    bet = place_bet(player)
    player.update_money(-bet)
    money = player.get_money()

    answer = "yes"
    while player.get_money() > 0 and answer == "yes":
        if run_game(deck, player, dealer):
            print("YAY YOU WON !!!!")
            player.update_money(bet * 2)
            print(f"you got {player.get_money()}$")
        else:
            print("LOSER YOU LOST")
            print(f"you got {player.get_money()}$")

        answer = input("continue ?: ")
        if answer != "yes":
            break

        print(f"You have {player.get_money()}$ \n \n")
        bet = place_bet(player)
        player.update_money(-bet)

        arr = deal_cards(deck)

        card1 = arr[0]
        card2 = arr[1]
        player = Player.Player(card1, card2)
        player.update_money(money)
        player.print_sum_of_player_and_cards()

        arr = deal_cards(deck)
        card3 = arr[0]
        card4 = arr[1]
        dealer = Player.Dealer(card3, card4)
        print(f"dealer's hand is: {card2.__str__()} \n")

    print("game stopped")



if __name__ == '__main__':
    main()
