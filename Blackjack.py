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

#Create a list of all possible suits and values for each of the 52 playing cards
suitlist = ["C", "D", "H", "S"]
valuelist = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

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
            cardstring = card.__str__()
            if "10" not in card.__str__():
                cardstring = " " + card.__str__()
            deckcards += cardstring
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

#Give each Card a value, with J/Q/K being equal to 10, and A initially being equal to 11. Add each card as a key to the dictionary (valdict), along with its int value
        if  value == "J" or value == "Q" or value == "K":
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
        self.redaces = 0
#Create instance variable Ace_Exists to keep track of how many reducable aces there are in a Player's hand
        self.Ace_Exists = 0

#Return the list of all cards as a string
    def __str__(self):
        handcards = ""
        for card in self.hand:
            handcards += card.__str__()
        return handcards

#Given the number of aces reduced to 1 (redaces), return the total value of all cards in a player's hand
    def cardval(self):
        sumcardval = 0
        for card in self.hand:
            if card != "" and card != " ":
                current_card = str(card).strip()
                sumcardval += (valdict[current_card])
        return sumcardval - (self.redaces * 10)

#Create methods addace and reduceAce to keep track of when aces are dealt, and when they have their values reduced 
    def addace(self):
        self.Ace_Exists += 1
    def reduceAce(self):
        self.redaces += 1
        self.Ace_Exists -= 1

#Create a function to showHands at the beginning of the round (keeping the appropriate cards hidden)
def showHands(opponent,dealer):
    print("Dealer shows %sfaceup" % (str(dealer)[3:]))
    print("You show %sfaceup" % (str(opponent)[3:]))
    print()
    print("You go first.")
    print()



#Create a function to go through the player's (opponent) turn
def opponentTurn(cardDeck,dealer,opponent):
#Initialize variable choice, in use later to determine how to proceed in the game
    choice = 0

#If one of the initial cards was an Ace, alert the player that it is currently worth 11
    if opponent.Ace_Exists >= 1:
        print("Assuming 11 points for an ace you were dealt for now.")
    print("You hold %s for a total of %s" % (opponent, opponent.cardval()))

#If the opponent has a blackjack, move on to the dealer's turn
    if opponent.cardval() == 21:
        print("21! My turn...")

#Ask the opponent to either hit or stay.
    else:
        choice = eval(input("1 (hit) or 2 (stay)? "))
#Create a loop. If the opponent busts, alert them and end the game. If they get a blackjack, move on to the dealer's turn. If they go over 21 and have any aces, reduce those as needed to keep the player from going bust
        while choice == 1:
            cardDeck.dealOne(opponent)
            if "A" in (str(opponent).strip()[-2:]):
                Player.addace(opponent)
            print()
            print("Card dealt: %s" % (str(opponent).strip()[-3:]))
            if opponent.cardval() == 21:
                choice = 4
            if opponent.cardval() > 21:
                if opponent.Ace_Exists >= 1:
                    Player.reduceAce(opponent)
                    print ("Over 21. Switching an ace from 11 points to 1.")
                    print ("New total: %s" % opponent.cardval())
                    print()
                else:
                    print("You have %s. You bust! Sorry!" % (opponent.cardval()))
                    choice = 3
            if opponent.cardval() < 21:
                print("You hold %s for a total of %s" % (opponent, opponent.cardval()))
                choice = eval(input("1 (hit) or 2 (stay)? "))
        if choice == 2:
            print("Staying with %s" % (opponent.cardval()))
            print()
        if choice == 4:
            print("21! My turn...")
    if choice == 3:
        return


def dealerTurn(cardDeck,dealer,opponent):
#If the player busted, end the game
    if opponent.cardval() > 21:
        print()
        print("Game over.")
        print("Final hands:")
        print("   Dealer:   ", dealer)
        print("   Opponent: ", opponent)
        return

#Initialize the dealer's turn, and display the current cards each player has
    print("Dealer's turn")
    print("Your hand: %sfor a total of %s" % (opponent, opponent.cardval()))
    print("Dealer's hand: %sfor a total of %s" % (dealer, dealer.cardval()))
    print()

#If one of the dealer's initial cards was an Ace, alert the player that it is currently worth 11
    if dealer.Ace_Exists >= 1:
        print("Assuming 11 points for an ace I was dealt for now.")

#If the dealer already has a score equal to or more than the opponent, the dealer wins and the game ends
    if dealer.cardval() == 21 and choice == 4:
        print("Dealer has 21. Dealer wins!")
        return
        print("Dealer has %s. Dealer wins!" % (dealer.cardval()))
        print()
        print("Game over.")
        print("Final hands:")
        print("   Dealer:   ", dealer)
        print("   Opponent: ", opponent)
        return
    elif dealer.cardval() >= opponent.cardval() and dealer.cardval() <= 21:
        print("Dealer has %s. Dealer wins!" % (dealer.cardval()))
        print()
        print("Game over.")
        print("Final hands:")
        print("   Dealer:   ", dealer)
        print("   Opponent: ", opponent)
        return
   

#Create an automatic loop for the dealer. If the opponent has a higher value hand, keep drawing cards. If the dealer busts, the opponent wins. If the dealer gets an equal or higher value to the opponent, the dealer wins
    while opponent.cardval() > (dealer.cardval()):
        cardDeck.dealOne(dealer)
        if "A" in (str(dealer).strip()[-2:]):
            Player.addace(dealer)
        print("Dealer hits: %s" % (str(dealer).strip()[-3:]))
        print("New total: %s" % dealer.cardval())
        print()
        if dealer.cardval() == 21:
            print("Dealer has 21. Dealer wins!")
            print()
            print("Game over.")
            print("Final hands:")
            print("   Dealer:   ", dealer)
            print("   Opponent: ", opponent)
            return
        if dealer.cardval() > 21:
            if dealer.Ace_Exists >= 1:
                Player.reduceAce(dealer)
                print ("Over 21. Switching an ace from 11 points to 1.")
                print ("New total: %s" % dealer.cardval())
                print()
            else:
                print("Dealer has %s. Dealer busts! You win." % (dealer.cardval()))
                print()
                print("Game over.")
                print("Final hands:")
                print("   Dealer:   ", dealer)
                print("   Opponent: ", opponent)
                return
        if dealer.cardval() >= opponent.cardval() and dealer.cardval() <= 21:
            print("Dealer has %s. Dealer wins!" % (dealer.cardval()))
            print()
            print("Game over.")
            print("Final hands:")
            print("   Dealer:   ", dealer)
            print("   Opponent: ", opponent)
            return


#Initialize the main function
def main():

#Initialize a deck (cardDeck), and print it
    cardDeck = Deck()
    print("Initial deck:")
    print(cardDeck)               
    
#Shuffle the deck with seed 50, then print it again
    random.seed()                 # leave this in for grading purposes
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)             

#Create two Players, the dealer and the opponent    
    dealer = Player()
    opponent = Player()
    

#Alternate dealing each player 2 cards.
    cardDeck.dealOne(opponent)    
    if "A" in (str(opponent).strip()[-2:]):
        Player.addace(opponent)
    cardDeck.dealOne(dealer)     
    if "A" in (str(dealer).strip()[-2:]):
        Player.addace(dealer)
    cardDeck.dealOne(opponent)    
    if "A" in (str(opponent).strip()[-2:]):
        Player.addace(opponent)
    cardDeck.dealOne(dealer)       
    if "A" in (str(dealer).strip()[-2:]):
        Player.addace(dealer)

#After dealing 4 cards total, print the deck
    print("Deck after dealing two cards each:")
    print(cardDeck)
    print()
    print()
    print()

#Call a function to show the hands at the start of the game
    showHands(opponent,dealer)

#Call a function opponentTurn to go through the player's turn
    opponentTurn(cardDeck,dealer,opponent)
#Call a function dealerTurn to go through the game's turn
    dealerTurn(cardDeck,dealer,opponent)


    
main()