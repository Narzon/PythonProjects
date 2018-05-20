#  File: Goldbach.py

#  Description: For a given range of even numbers starting from at least 4, print for each even number all pairs of unique prime addends (representing Goldbach's conjecture n = a + b)

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: February 25, 2016

#  Date Last Modified: February 25, 2016


def main():
#Define function "is_prime(n)" to check for prime numbers
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

#Prompt user for lower and upperlimit, assign to variables "lolimit" and "uplimit" respectively
   lolimit = eval(input("Enter the lower limit: "))
   uplimit = eval(input("Enter the upper limit: "))

#Error check; make sure the lower limit is at least 4, both limits are even numbers, and the lower limit is strictly less than the upper limit. Otherwise, prompt user for inputs again
   while (lolimit < 4) or (lolimit % 2 != 0) or (uplimit % 2 != 0) or (lolimit >= uplimit):
      lolimit = eval(input("Enter the lower limit: "))
      uplimit = eval(input("Enter the upper limit: "))
#Define variables "a" and "b" for Goldbach's conjecture
   a = 0
   b = 0   
#Set up a loop to continue running from the lower limit until the upper limit
   while (lolimit <= uplimit):
#For each part of the cycle, start by printing variable "lolimit", the "n" of "n = a + b"
      print (str(lolimit), end = ' ')
#As long as variable "a" is not prime, or the difference "lolimit - a" is not prime, keep adding 1 to "a"
      while not is_prime(lolimit - a):
         a += 1
         while not is_prime(a):
            a += 1
#Once "a" fits the criteria, define "b" by "b = lolimit - a"
      b = (lolimit - a)
#Until "a" becomes greater than "b" (to avoid backwards repeats), keep adding 1 to "a" and redefining "b", and print (= a + b) on the same line whenever the conditions are met for Goldbach's conjecture
      while (a <= b):
         if is_prime(a) and is_prime(b) and (b >= a) and (lolimit == a + b):
            print("=", a, "+", b, end = ' ')
            a += 1
         else:
            a +=1
            b = (lolimit - a)
#Reset the value of "a" and continue the cycle with the next even number by adding 2 to "lolimit"
      a = 0
      lolimit += 2
#Finish the print line
      print()
main()