#  File: Deal.py

#  Description: Simulate the "Monty Hall" process for a given number of attempts, and display the probability of winning by switching or not switching doors along with the results for each attempt.

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: March 4, 2016

#  Date Last Modified: March 4, 2016

#import random to use RNG to simulate which door holds the prize and which door is guessed in each attempt
import random
def main():

#prompt the user to input how many times the program should go through the process
   num_play = eval(input("Enter number of times you want to play: "))

#establish the variables num_wins (for the number of times the game is "won" by switching doors) and counter (for the while-loop)
   num_wins = 0
   counter = 1

#print the column headers
   print ()
   print ("  Prize      Guess       View    New Guess ")

#set the while loop to run for as many times as the user inputs
   while (counter <= num_play):

#set the prize and guess doors to any number between 1 and 3 (inclusive)
      prize = random.randint(1, 3)
      guess = random.randint(1, 3)

#set the "view" door as different to the guess when guess and prize are the same, or to the unclaimed number if guess and prize are different
      if guess == prize and prize == 1:
         view = 2
      elif guess == prize and prize == 2:
         view = 3
      elif guess == prize and prize == 3:
         view = 1
      if guess != prize:
         view = 6 - (guess + prize)

#set the newGuess variable equal to whichever number wasn't guessed initially and wasn't viewed
      newGuess = 6 - (guess + view)

#if newGuess is equal to the prize, then the player "wins", and 1 is added to the num_wins variables
      if newGuess == prize:
         num_wins += 1

#print the variables associated with Prize, Guess, View, and New Guess underneath the respective headers, and add 1 to counter to continue the loop
      print ("   ",prize,"        ",guess,"        ",view,"        ",newGuess)
      counter += 1
   print ()

#compute the probability of winning by switching doors (probWinswitch) and then subtract that from 1 to get the probability of winning by staying on the same door (probWinstay)
   probWinswitch = num_wins / num_play
   probWinstay = 1 - probWinswitch

#print the probability of both scenarios, to 2 decimal places
   print ("Probability of winning if you switch = %.2f" % (probWinswitch))
   print ("Probability of winning if you do not switch = %.2f" % (probWinstay))
main()

