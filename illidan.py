import random
def main():
   x = eval(input("Enter drop chance percent: "))
   y = eval(input("Enter number of runs: "))
   if x <= 0 or y <= 0:
      x = eval(input("Enter drop chance percent: "))
      y = eval(input("Enter number of runs: "))
   x = x / 100
   chance = 1 - ( (1 - x) ** y)
   chance = round((chance * 100), 0)
   print (chance,"% of seeing this item drop in",(y),"runs.")
main()