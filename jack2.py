#  File: Blackjack.py
#  Description: Play one round of Blackjack against a computer
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: September 20, 2016
#  Date Last Modified: September 21, 2016


#Import random for shuffling, and initialize a dictionary (valdict) for card values 
import random
valdict = {}

#Create a list of all possible suits and values for each of the 52 playing cards. In this case, T=10 as a value
suitlist = ["C", "D", "H", "S"]
valuelist = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

#Define a Deck, which creates a deck of 52 Cards when initialized
class Deck:
    def __init__(self):
        self.cardList = []
        for i in suitlist:
            for j in valuelist:
                self.cardList.append(Card(i, j))

#Define a method to shuffle the deck
    def shuffle(self):
        random.shuffle(self.cardList)

#Define a method to deal the top card of the Deck to a given person's hand (Player), removing the card from the Deck
    def dealOne(self, person):
        (person.hand).append(self.cardList[0])
        (person.hand).append(" ")
        self.cardList.remove(self.cardList[0])

#When called to print, return the deck in neat columns by going to next line every 12 cards
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

#Create a Card, given a suit and value
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

#Give each Card a value, with T/J/Q/K being equal to 10, and A initially being equal to 11. Add each card as a key to the dictionary (valdict), along with its int value
        if  value == "J" or value == "Q" or value == "K" or value =="T":
            value = 10
        elif value == "A":
            value = 11
        else:
            value = int(value)
        valdict["%s%s" % (self.value, self.suit)] = value
        self.actualvalue = value

#When called, return the card in the proper format
    def __str__(self):
        return self.value + self.suit

#Create a Player. When initialized, create a new hand of cards for each player as an empty list
class Player:
    def __init__(self):
        self.hand = []

#Return the list of all cards as a string
    def __str__(self):
        handcards = ""
        for card in self.hand:
            handcards += card.__str__()
        return handcards

#Given the number of aces reduced to 1 (redaces), return the total value of all cards in a player's hand
    def cardval(self, redaces):
        sumcardval = 0
        for card in self.hand:
            if card != "" and card != " ":
                current_card = str(card).strip()
                sumcardval += (valdict[current_card])
        return sumcardval - (redaces * 10)


#Initialize the main function
def main():

#Initialize a deck (cardDeck), and print it
    cardDeck = Deck()
    print("Initial deck:")
    print(cardDeck)               
    
#Shuffle the deck with seed 50, then print it again
#    random.seed(50)                 # leave this in for grading purposes
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)             

#Create two Players, the dealer and the opponent    
    dealer = Player()
    opponent = Player()
    
#Create variables Ace_Exists (and Ace_ExistsD for the dealer) to keep track of how many aces either player currently has in their hands which are currently worth 11
    Ace_Exists = 0
    Ace_ExistsD = 0

#Alternate dealing each player 2 cards
    cardDeck.dealOne(opponent)    
    if "A" in (str(opponent).strip()[-2:]):
        Ace_Exists += 1
    cardDeck.dealOne(dealer)     
    if "A" in (str(dealer).strip()[-2:]):
        Ace_ExistsD += 1
    cardDeck.dealOne(opponent)    
    if "A" in (str(opponent).strip()[-2:]):
        Ace_Exists += 1
    cardDeck.dealOne(dealer)       
    if "A" in (str(dealer).strip()[-2:]):
        Ace_ExistsD += 1

#After dealing 4 cards total, print the deck
    print("Deck after dealing two cards each:")
    print(cardDeck)
    print()
    print()
    print()

#At the start of the game, reveal each player's face-up card
    dealershand = str(dealer)
    opponentshand = str(opponent)
    print("Dealer shows %sfaceup" % (dealershand[3:]))
    print("You show %sfaceup" % (opponentshand[3:]))

    print()
    print("You go first.")
    print()

#If one of the initial cards was an Ace, alert the player that it is currently worth 11
    if Ace_Exists >= 1:
        print("Assuming 11 points for an ace you were dealt for now.")
    print("You hold %s for a total of %s" % (opponent, opponent.cardval(0)))

#Create variables redaces (redacesD for dealer) to keep track of many aces in each player's hand is being reduced to a value of 1
    redaces = 0
    redacesD = 0

#Initialize variable choice, in use later to determine how to proceed in the game
    choice = 0

#If the opponent has a blackjack, move on to the dealer's turn
    if opponent.cardval(0) == 21:
        print("21! My turn...")

#Ask the opponent to either hit or stay. Each hit, continue to track any aces with Ace_Exists
    else:
        choice = eval(input("1 (hit) or 2 (stay)? "))
        print()
#Create a loop. If the opponent busts, alert them and end the game. If they get a blackjack, move on to the dealer's turn. If they go over 21 and have any aces, reduce those as needed to keep the player from going bust
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

#Initialize the dealer's turn, and display the current cards each player has
    print("Dealer's turn")
    print("Your hand: %sfor a total of %s" % (opponent, opponent.cardval(redaces)))
    print("Dealer's hand: %sfor a total of %s" % (dealer, dealer.cardval(redacesD)))
    print()

#If the dealer already has a score equal to or more than the opponent, the dealer wins and the game ends
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

#Create an automatic loop for the dealer. If the opponent has a higher value hand, keep drawing cards. If the dealer busts, the opponent wins. If the dealer gets an equal or higher value to the opponent, the dealer wins
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