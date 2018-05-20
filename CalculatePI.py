#  File: CalculatePI.py

#  Description: Estimate Pi to various degrees of precision using random number generation and the "dart-board" method for different amounts of darts thrown

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: February 29, 2016

#  Date Last Modified: February 29, 2016

#import databases "math" (for the value of canonical pi) and "random" (for random number generation)
import math
import random

#define the function "computePI" to estimate the value of Pi within a given number of darts thrown
def computePI (numThrows):
#establish the variable sum_darts to represent the number of darts within the "circle" of the dartboard, and initialize a counter for the while loop
   sum_darts = 0
   counter = 1
#set the while loop to last for as many throws as specified in the function input
   while (counter <= numThrows):
#ugenerate random numbers between the values of -1.0 and 1.0 (assuming the "dartboard" has a radius of 1)
      xPos = random.uniform (-1.0, 1.0)
      yPos = random.uniform (-1.0, 1.0)
#use the coordinate distance formula sqrt(x^2 + y^2) to find the distance any given "dart" is from the center of the circle. if the distance is strictly less than the radius (1), add 1 to sum_darts
      if (((xPos ** 2) + (yPos ** 2)) ** (1/2)) < 1:
         sum_darts += 1
#add 1 to the counter to continue "throwing darts"
      counter += 1
#return the estimated value of Pi
   return (4 * (sum_darts) / (numThrows))



def main ():
   print("Computation of PI using Random Numbers")
   print()

#establish the variables calcPi (for Pi calculated with the function computePi), diff (for the differences between calcPi and canonical Pi), and realpi (for canonical pi). also, start the input "num" at 100 darts
   calcPi = 0
   diff = 0
   num = 100
   realpi = math.pi
#set the print loop to run from the initial num value (100) to 10000000, in increments of 10 times
   while (num <= 10000000):
      calcPi = computePI (num)
      diff = calcPi - realpi
#print the line for each increment, using formatting rules for fixed width and fixed floating decimal points
      print (("num ="),"{0: <8}".format(num),"  Calculated PI =",format(calcPi, ".6f"),"  Difference =",format(diff, "+.6f"))
      num = num * 10
   print()
   print("Difference = Calculated PI - math.pi")
main()

