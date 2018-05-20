#  File: Hailstone.py

#  Description: For a given range of natural numbers, compute which number will go through the greatest number of cycles in the Hailstone Sequence before reaching 1, and state how many cycles that is

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: February 8, 2016

#  Date Last Modified: February 8, 2016


def main():

#Set up the function "is palindromic"
   def is_palindromic (n):
     return (n == rev_num(n))

#Set up the function "rev_num"
   def rev_num (n):
     rev_n = 0
     while (n > 0):
       rev_n = rev_n * 10 + (n % 10)
       n = n // 10
     return rev_n

#Prompt user for start and end numbers for a range using varibles starting_num and ending_num
   starting_num = eval(input("Enter starting number of the range: "))
   ending_num = eval(input("Enter ending number of the range: "))

#Error check to make sure both inputs are positive, and that the ending number is greater than the starting number
   while starting_num > ending_num or starting_num <= 0 or ending_num <= 0:
      starting_num = eval(input("Enter starting number of the range: "))
      ending_num = eval(input("Enter ending number of the range: "))

#Initiate the variables, max_num for the number in the range with the most cycles, max_cycle for the most cycles
   max_num = 0
   max_cycles = 0
#Initiate the variables, cycles for the number of cycles for each integer, and num for the number going through the sequence each time
   cycles = 0
   num = 0
   

#Set up a loop to continue running the Hailstone sequence until reaching the end of the range
   while (starting_num <= ending_num):
#Define variable num first as the starting number, and every subsequent integer afterwards 
      num = starting_num
#Set up the Hailstone sequence loop to run for each integer in the range until the resulting number is 1
      while not is_palindromic (num):  
         num = num + rev_num (num)
         cycles = cycles + 1
#Redefine the varibles max_num and max_cycles each time the cycles for an integer are greater than or equal to the previous highest ("equal to" is important, to make sure the higher number is prefered in the case of two numbers with equal cycles)
      if (cycles >= max_cycles):
         max_num = starting_num
         max_cycles = cycles
#Before continuing the cycle, add 1 to starting_num to go to next integer and reset current cycles back to 0
      starting_num = starting_num + 1
      cycles = 0


#Print the result, turning the max_cycles variable into a string to add a period at the end of the string
   print("The number",max_num,"has the longest cycle length of",(str(max_cycles)) + ".")

main()