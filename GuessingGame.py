#  File: GuessingGame.py

#  Description: Guess a number a user thinks of between 1 and 100 inclusive using binary search

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 13, 2016

#  Date Last Modified: April 13, 2016


def main():

#Print the opening statements
	print("Guessing Game")
	print()
	print("Think of a number between 1 and 100 inclusive.")
	print("And I will guess what it is in 7 tries or less.")
	print()

#Ask the user if they're ready, assign the input to variable qa
	qa = input("Are you ready? (y/n): ")

#If the user does not answer "y" or "n", keep repeating the question
	while qa != "n" and qa != "y":
		qa = input("Are you ready? (y/n): ")

#If the user answers "n", print "Bye" and terminate the program
	if qa == "n":
		print("Bye")
		return
	print()

#Set the hi and lo variables to 101 and 0 respectively (to keep answers inclusive)
	hi = 101
	lo = 0

#Set the variable condition = 1 to keep track of the number of guesses, and to act as a loop counter
	condition = 1

#Set the guessing loop to run for a maximum of 7 guesses
	while condition < 8:

#Establish the guess for each new iteration of the loop to be the average of the hi and lo values
		guess = (hi + lo) // 2

#Display the guess number and offer the guess to the user
#Prompt the user to answer -1, 0, or 1; if the user does not answer with one of the listed responses, repeat the guess and keep asking
#Read the inputs as strings and do not eval, to avoid errors with non-integer inputs
		print("Guess  %s :  The number you thought was %s" % (condition, guess))
		answer = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
		while answer != "1" and answer != "0" and answer != "-1":
			print()
			print("Guess  %s :  The number you thought was %s" % (condition, guess))
			answer = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")

#If the user answers "0" (for a correct guess), print "Thank you for playing the Guessing Game." and terminate the program
		if answer == "0":
			print()
			print("Thank you for playing the Guessing Game.")
			return

#If the user answers "1" (for a high guess), reassign the hi variable to the current guess and continue to the next loop iteration
		if answer == "1":
			hi = guess
			condition += 1

#If the user answers "-1" (for a low guess), reassign the lo variable to the current guess and continue to the next loop iteration
		if answer  == "-1":
			lo = guess
			condition += 1
		print()

#If the user does not answer 0 on the 7th guess, print that they have made an error and terminate the program
	if condition == 8:
		print("Either you guessed a number out of range or you had an incorrect entry.")
		return
main()

