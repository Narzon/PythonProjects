#  File: DNA.py

#  Description: (WITH EXTRA CREDIT PROVISION) Given a file of a number DNA pairs, print the longest common sequences that exist within each pair

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: March 24, 2016

#  Date Last Modified: March 24, 2016

#import string functions
import string
def main():

#open the dna.txt files and assign it to the string variable "strands"
   strands = open('dna.txt', 'r')
  
#assign the first line of the file to "pairs"; this will be the number of pairs of DNA strands
   pairs = eval(strands.readline())

#print the header statement
   print("Longest Common Sequences")

#set a while loop to run for as many pairs as specified above
   counter = 1
   while counter <= pairs:
      print()

#use readline to assign the two lines in each pair to variables string1 and string2, and convert them to uppercase and strip each line
      string1 = strands.readline().upper().strip( )
      string2 = strands.readline().upper().strip( )
     
#initiate variables: 

#pairs_exist will determine whether or not to print "No Common Sequence Found" 
#needs_justifying will add necessary formatting spaces after the first common sequence in a pair
#list_values will keep track of whether a common sequence has already been printed to avoid repeats

      pairs_exist = 0
      needs_justifying = 0
      list_values = []

#print the "Pair n:" start of each line, where n is the current pair
      print("Pair %s:"% str(counter), end = " ")


#set a flag condition to terminate the while loop when the first (and longest) common sequences are found
      flag = True

#assign substrings in string1 to variable piece
      wnd = len(string1)
      while (wnd > 0) and flag:
         start_idx = 0
         while ((start_idx + wnd) <= len(string1)):
            piece = string1[start_idx : start_idx + wnd]

#use the find function to determine if a substring from string1 appears in string2 (and hasn't already appeared in list_values); if so append it to list_values, and then print it (adding spaces if it's not the first common sequence in the pair)
            if (string2.find(piece) != -1) and (piece not in list_values):
               list_values.append(piece)
               if needs_justifying == 0:
                  print(piece)
                  needs_justifying = 1
               else:
                  print("       ", piece)

#add 1 to pairs_exist, so not to print "No Common Sequence", and set flag to False to prevent smaller substrings from being examined
               pairs_exist += 1
               flag = False
            start_idx += 1
         wnd = wnd - 1
      if pairs_exist == 0:
         print("No Common Sequence Found")

#add to the counter to continue to first while loop
      counter += 1
main()