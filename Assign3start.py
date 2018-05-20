def main():
#Prompt user for start and end numbers for a range using varibles starting_num and ending_num
   starting_num = eval(input("Enter starting number of the range: "))
   ending_num = eval(input("Enter ending number of the range: "))

#Error check to make sure the starting number is positive, and the ending number is greater than the starting number
   while starting_num > ending_num or starting_num <= 0:
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
#Define varibles num first as the starting number, and every subsequent integer 
      num = starting_num
#Set up the Hailstone sequence loop to run for each integer in the range until the resulting number is 1
      while (num != 1):
         
         if (num % 2 == 0):
            num = num / 2
            cycles = cycles + 1
         else:
            num = num * 3 + 1
            cycles = cycles + 1
#Redefine the varibles max_num and max_cycles each time the cycles for an integer are greater than or equal to the previous highest
         if (cycles >= max_cycles):
            max_num = starting_num
            max_cycles = cycles
#Before continuing the cycle, add 1 to starting_num to go to next integer and reset current cycles back to 0
      starting_num = starting_num + 1
      cycles = 0


#Print the result
   print("The number",max_num,"has the longest cycle length of",(str(max_cycles)) + ".")

main()

