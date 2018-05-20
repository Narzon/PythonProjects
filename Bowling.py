#  File: Bowling.py
#  Description: Reading a file of bowling scores, calculate running totals for each game
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: September 7, 2016
#  Date Last Modified: September 8, 2016


#Create the Process that will take the list of characters from each read line, and create the scoreboard
def Process (st):

#Create the variable sum to keep track of the running total score for each ten-frame game
   sum = 0

#Insert spaces after each "X" character to allow for each strike to make up its own pair during a Frame (keeping careful not to add spaces after Frame 10 strikes)
   for i in range(len(st) - 4, -1, -1):
      if st[i] == "X":
         st.insert((i + 1), " ")
   if len(st) < 20:
      st.insert(17, " ")

#Create a separate list, stval, to keep track of the integer values for each corresponding string character (for use during calculations)
   stval = []
   for i in range(0, len(st)):
      if st[i].isdigit():
         stval.append(int(st[i]))
      if st[i] == "X":
         stval.append(10)
      if st[i] == "/":
         prevnum = (stval[i - 1])
         diffnum = 10 - prevnum
         stval.append(diffnum)
      if st[i] == "-" or st[i] == " ":
         stval.append(0)


#Begin printing the scoreboard layout for the game
   print ("  1   2   3   4   5   6   7   8   9    10")
   print ("+---+---+---+---+---+---+---+---+---+-----+")
   
#List the string characters for the score in pairs for each Frame, with Frame 10 potentially having 3 characters (determine this by the length of the entire list st)
   for i in range (0, 18, 2):
      print ("|%s %s" % (st[i], st[i + 1]), end = "")
   if len(st) == 20:
      print ("|%s %s" % (st[-2], st[-1]), end = "")
   if len(st) == 21:
      print ("|%s %s %s" % (st[-3], st[-2], st[-1]), end = "")

#Initialize a counter to keep track of how many times the score has been calculated, and to determine when the final score has been determined (for formatting reasons)
   counter = 0

#Create a loop for games (st) which have 2 rolls in Frame 10
   if len(st) == 20:
      print("  |")
      for i in range (0, 19, 2):
         sum += stval[i] + stval[i + 1]
         if st[i] == "X" and i < 18:
            if st[i + 2] != "X":
               sum += stval[i + 2] + stval[i + 3]
            else:
               sum += stval[i + 2] + stval[i + 4]
         elif st[i] == "X" and i == 18:
            sum += stval[19]
         if st[i + 1] == "/":
            sum += stval[i + 2]
         if counter != 9:               
            print("|", end ="")
            print("{0: >3}".format("%s" % (sum)), end = "")
         else:
            print("|", end ="")
            print("{0: >6}".format("%s|" % (sum)), end = "")
         counter += 1

#Create a loop for games (st) which have 3 rolls in Frame 10
   if len(st) == 21:
      print("|")
      for i in range (0, 19, 2):
         sum += stval[i] + stval[i + 1]
         if st[i] == "X":
            if i < 16:
               if st[i + 2] != "X":
                  sum += stval[i + 2] + stval[i + 3]
               else:
                  sum += stval[i + 2] + stval[i + 4]
            if i == 16:
               sum += stval[i + 2] + stval[i + 3]
            if i == 17:
               sum += stval[19]
            if i == 18:
               sum += stval[20] 
         if st[i + 1] == "/":
            sum += stval[i + 2]
         if counter != 9:               
            print("|", end ="")
            print("{0: >3}".format("%s" % (sum)), end = "")
         else:
            print("|", end ="")
            print("{0: >6}".format("%s|" % (sum)), end = "")
         counter += 1
   print()

#Close the score box
   print ("+---+---+---+---+---+---+---+---+---+-----+")
   print()

#In the main function, open the file "scores.txt" in read mode, assign each line as a variable, strip line, split line into a list of string characters, and run the previous function Process for each line's list
def main():
   all_scores = open("scores.txt", "r")
   for line in all_scores:
      line = line.strip()
      line = line.split()
      line = Process(line)

main()
