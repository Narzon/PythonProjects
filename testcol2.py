#  File: Hailstone.py

#  Description: For a given range of natural numbers, compute which number will go through the greatest number of cycles in the Hailstone Sequence before reaching 1, and state how many cycles that is

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: February 8, 2016

#  Date Last Modified: February 8, 2016


def main():
#Define function is_prime	
   def is_prime (n):
      if (n == 1):
         return False

      limit = int(n ** 0.5) + 1
      divisor = 2
      while (divisor < limit):
         if (n % divisor == 0):
            return False
         divisor += 1
      return True

#Prompt user for start and end numbers for a range using varibles starting_num and ending_num
   lolimit = eval(input("Enter the lower limit: "))
   uplimit = eval(input("Enter the upper limit: "))

#Error check to make sure both inputs are positive, and that the ending number is greater than the starting number
   while (lolimit < 4) or (lolimit % 2 != 0) or (uplimit % 2 != 0) or (lolimit >= uplimit):
      lolimit = eval(input("Enter the lower limit: "))
      uplimit = eval(input("Enter the upper limit: "))
   a = 0
   b = 0   
#Set up a loop to continue running the Hailstone sequence until reaching the end of the range
   while (lolimit <= uplimit):
      print (str(lolimit), end = ' ')
#Set up the Hailstone sequence loop to run for each integer in the range until the resulting number is 1
      while not is_prime(lolimit - a):
         a += 1
         while not is_prime(a):
            a += 1
      b = (lolimit - a)
      while (a <= b):
         if is_prime(a) and is_prime(b) and (b >= a) and (lolimit == a + b):
            print("=", a, "+", b, end = ' ')
            a += 1
         else:
            a +=1
            b = (lolimit - a)
      a = 0
      lolimit += 2
      print()
main()