#  File: FibonacciBase.py

#  Description: Given a decimal integer, convert the integer into a binary number in the Fibonacci base

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 30, 2016

#  Date Last Modified: April 30, 2016


#Define a function convert_fib_base to create a list of numbers representing the Fibonacci sequence, which runs until it reaches a number greater than a given num
def convert_fib_base (num):

#Initialize the Fibonacci sequence, starting from the second "1"
	fib_seq = []
	fib_seq += 1, 2
#Continue appending numbers to the Fibonacci sequence list, breaking if the current value exceeds the given num. Return this list
	for i in range(2, num):
		fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
		if fib_seq[i] >= num:
			break
	return fib_seq



def main():

#Prompt the user to give a number, then use the function convert_fib_base to return a list representing the Fibonacci sequence from the second "1" to a value greater than the input num
	enternum = eval(input("Enter a number: "))
	fib_seq = convert_fib_base(enternum)

#Reverse the Fibonacci sequence list
	fib_seq.reverse()
	print("%s = " % enternum, end ="")
	
#Create a flag to tell the loop when to start printing "0"s instead of nothing
	flag = False

#Create a loop that goes through each term in the reverse Fibonacci sequence
	for i in range (0, len(fib_seq)):

#If the current Fibonacci number is greater than the current enternum value, either skip over it, or (if flagged by a previous "1"), print "0"
		if fib_seq[i] > enternum:
			if flag:
				print("0", end="")

#If the current Fibonacci number is less than the current enternum value, print "1", subtract that Fibonacci number to get a new enternum value, and set flag to True to begin printing "0"s
		elif fib_seq[i] < enternum:
			print("1", end="")
			enternum -= fib_seq[i]
			flag = True

#If the current Fibonacci number is equal to the current enternum value, the sequence is finished; print "1", and set enternum to "0" so all further Fibonacci numbers will return "0"s
		elif fib_seq[i] == enternum:
			print("1", end="")
			enternum = 0
			flag = True
	print(" (fib)")

main()