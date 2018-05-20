import random
valdict = {}
suitlist = ["H", "D", "S", "C"]
valuelist = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

class Deck:
    def __init__(self):
        self.cardList = []
        for i in suitlist:
            for j in valuelist:
                self.cardList.append(Card(i, j))
    def shuffle(self):
        random.shuffle(self.cardList)

    def dealOne(self, person):
        (person.hand).append(self.cardList[0])
        (person.hand).append(" ")
        self.cardList.remove(self.cardList[0])

    def __str__(self):
        counter = 0
        deckcards = ""
        for card in self.cardList:            
            deckcards += card.__str__()
            if counter != 12:
                counter += 1
                deckcards += " "
            else:
                deckcards += "\n"
                counter = 0
        return deckcards

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

#Give each Card a value
        if value == "T" or value == "J" or value == "Q" or value == "K":
            value = 10
        elif value == "A":
            value = 11
        else:
            value = int(value)
        valdict["%s%s" % (self.suit, self.value)] = value
        self.actualvalue = value

    def __str__(self):
        return self.suit + self.value


class Player:
    def __init__(self):
        self.hand = []
    def __str__(self):
        handcards = ""
        for card in self.hand:
            handcards += card.__str__()
        return handcards
    def cardval(self, redaces):
        sumcardval = 0
        for card in self.hand:
            if card != "" and card != " ":
                current_card = str(card).strip()
                sumcardval += (valdict[current_card])
        return sumcardval - (redaces * 10)



def showHands(opponent, dealer):
    dealershand = str(dealer)
    opponentshand = str(opponent)
    if len(dealershand) == 6:
        print("Dealer shows %s faceup" % (dealershand[3:]))
        print("You show %s faceup" % (opponentshand[3:]))
    else:
        print("Player's cards are:", opponent)
        print("Opponent's card are:", dealer)
    return





def main():
    cardDeck = Deck()
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
#    random.seed(50)                 # leave this in for grading purposes
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see what resulted from your shuffle




    
    dealer = Player()
    opponent = Player()
    

    Ace_Exists = 0
    Ace_ExistsD = 0
    cardDeck.dealOne(opponent)      # face up
    if "A" in (str(opponent).strip()[-2:]):
        Ace_Exists += 1
    cardDeck.dealOne(dealer)        # face down
    if "A" in (str(dealer).strip()[-2:]):
        Ace_ExistsD += 1
    cardDeck.dealOne(opponent)      # face up
    if "A" in (str(opponent).strip()[-2:]):
        Ace_Exists += 1
    cardDeck.dealOne(dealer)        # face up
    if "A" in (str(dealer).strip()[-2:]):
        Ace_ExistsD += 1
    
    print("Deck after dealing two cards each:")
    print(cardDeck)
    print()
    print()
    print()

    dealershand = str(dealer)
    opponentshand = str(opponent)
    print("Dealer shows %sfaceup" % (dealershand[3:]))
    print("You show %sfaceup" % (opponentshand[3:]))

    print()
    print("You go first.")
    print()
    if Ace_Exists >= 1:
        print("Assuming 11 points for an ace you were dealt for now.")
    print("You hold %s for a total of %s" % (opponent, opponent.cardval(0)))

    redaces = 0
    redacesD = 0

    choice = 0

    if opponent.cardval(0) == 21:
        print("21! My turn...")
    else:
        choice = eval(input("1 (hit) or 2 (stay)? "))
        print()
        while choice == 1:
            cardDeck.dealOne(opponent)
            if "A" in (str(opponent).strip()[-2:]):
                Ace_Exists += 1
            print("Card dealt: %s" % (str(opponent).strip()[-2:]))
            if opponent.cardval(redaces) == 21:
                choice = 4
            if opponent.cardval(redaces) > 21:
                if Ace_Exists >= 1:
                    redaces += 1
                    Ace_Exists -= 1
                    print ("Over 21. Switching an ace from 11 points to 1.")
                    print ("New total: %s" % opponent.cardval(redaces))
                    print()
                else:
                    print("You have %s. You bust! Sorry!" % (opponent.cardval(redaces)))
                    choice = 3
            if opponent.cardval(redaces) < 21:
                print("You hold %s for a total of %s" % (opponent, opponent.cardval(redaces)))
                choice = eval(input("1 (hit) or 2 (stay)? "))
        if choice == 2:
            print("Staying with %s" % (opponent.cardval(redaces)))
            print()
        if choice == 4:
            print("21! My turn...")
    if choice == 3:
        print()
        print("Game over.")
        print("Final hands:")
        print("   Dealer:   ", dealer)
        print("   Opponent: ", opponent)
        return

    print("Dealer's turn")
    print("Your hand: %sfor a total of %s" % (opponent, opponent.cardval(redaces)))
    print("Dealer's hand: %sfor a total of %s" % (dealer, dealer.cardval(redacesD)))
    print()

    if dealer.cardval(redacesD) == 21 and choice == 4:
        print("Dealer has 21. Dealer wins!")
        return
        print("Dealer has %s. Dealer wins!" % (dealer.cardval(redacesD)))
        print()
        print("Game over.")
        print("Final hands:")
        print("   Dealer:   ", dealer)
        print("   Opponent: ", opponent)
        return
    elif dealer.cardval(redacesD) >= opponent.cardval(redaces):
        print("Dealer has %s. Dealer wins!" % (dealer.cardval(redacesD)))
        print()
        print("Game over.")
        print("Final hands:")
        print("   Dealer:   ", dealer)
        print("   Opponent: ", opponent)
        return


    while opponent.cardval(redaces) > (dealer.cardval(redacesD)):
        cardDeck.dealOne(dealer)
        if "A" in (str(dealer).strip()[-2:]):
            Ace_ExistsD += 1
        print("Dealer hits: %s" % (str(dealer).strip()[-2:]))
        print("New total: %s" % dealer.cardval(redacesD))
        if dealer.cardval(redacesD) == 21:
            print()
            print("Dealer has 21. Dealer wins!")
            print()
            print("Game over.")
            print("Final hands:")
            print("   Dealer:   ", dealer)
            print("   Opponent: ", opponent)
            return
        if dealer.cardval(redacesD) > 21:
            if Ace_ExistsD >= 1:
                redacesD += 1
                Ace_ExistsD -= 1
                print()
                print ("Over 21. Switching an ace from 11 points to 1.")
                print ("New total: %s" % dealer.cardval(redacesD))
            else:
                print()
                print("Dealer has %s. Dealer busts! You win." % (dealer.cardval(redacesD)))
                print()
                print("Game over.")
                print("Final hands:")
                print("   Dealer:   ", dealer)
                print("   Opponent: ", opponent)
                return
        if dealer.cardval(redacesD) >= opponent.cardval(redaces) and dealer.cardval(redacesD) <= 21:
            print()
            print("Dealer has %s. Dealer wins!" % (dealer.cardval(redacesD)))
            print()
            print("Game over.")
            print("Final hands:")
            print("   Dealer:   ", dealer)
            print("   Opponent: ", opponent)
            return
    
main()