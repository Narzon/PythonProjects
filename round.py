import math
import random

def computePI (numThrows):
   sum_darts = 0
   counter = 1
   while (counter <= numThrows):
      xPos = random.uniform (-1.0, 1.0)
      yPos = random.uniform (-1.0, 1.0)
      if (((xPos ** 2) + (yPos ** 2)) ** (1/2)) < 1:
         sum_darts += 1
      counter += 1
   return (4 * (sum_darts) / (numThrows))

def main ():
   print("Computation of PI using Random Numbers")
   print()

   calcPi = 0
   diff = 0
   num = 100
   realpi = math.pi
   while (num <= 10000000):
      calcPi = computePI (num)
      diff = calcPi - realpi
      print (("num ="),"{0: <8}".format(num),"  Calculated PI =",format(calcPi, '.6f'),"   Difference =",format(diff, '+.6f'))
      num = num * 10
   print()
   print("Difference = Calculated PI - math.pi")
main()

