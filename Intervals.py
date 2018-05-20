#  File: Intervals.py

#  Description: Given a file of intervals, collapse all overlapping intervals and print them as a list of tuples. Then, print them in order of ascending size.

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 19, 2016

#  Date Last Modified: April 20, 2016

def main():

#Open the file "intervals.txt.", and go line by line stripping and splitting each interval
   in_File = open("intervals.txt", "r")
   list_pairs = []
   for line in in_File:
      line = line.strip()
      line = line.split()

#Convert each number in each interval to an integer, then convert each interval to a tuple
      for i in range (0, 2):
         line[i] = int(line[i])
      line = tuple(line)

#Append each tuple to a list, "list_pairs"
      list_pairs.append(line)


#Sort the list of tuples
   list_pairs = sorted(list_pairs)

   print("Non-intersecting Intervals:")

#Create a list newlist_p to hold each interval that has been fully collapsed
   newlist_p = []

#For each interval in list_pairs, check the second number against the number in the next interval
   for x in range (0, len(list_pairs) - 1):
      if list_pairs[x][1] >= list_pairs[x + 1][0]: 

#If the intervals overlap, check that they don't overlap completely. If they overlap partially, replace the next interval with the collapsed interval
         if list_pairs[x][1] <= list_pairs[x + 1][1]:
            newtup = (list_pairs[x][0], list_pairs[x + 1][1])
            list_pairs[x + 1] = newtup

#If the inverals overlap completely, replace the next interval with the current one
         else:
            list_pairs[x + 1] = list_pairs[x]

#If the intervals do not overlap, append the fully-collapsed current interval to newlist_p
      else:
         newlist_p.append(list_pairs[x])

#Append the final collapsed interval
   newlist_p.append(list_pairs[-1])


#Print the collapsedintervals
   for i in newlist_p:
      print (i)

   print()
   print("Non-intersecting Intervals in order of size:")

#Run a sorting algorithm for newlist_p, based on the value of the difference of each interval
   for i in range (len(newlist_p) - 1):
      min_diff = (newlist_p[i][1] - newlist_p[i][0])
      min_idx = i
      min_diffval = newlist_p[i]
      for j in range (i + 1, len(newlist_p)):
         if (newlist_p[j][1] - newlist_p[j][0]) < min_diff:
            min_diff = (newlist_p[j][1] - newlist_p[j][0])
            min_diffval = newlist_p[j]
            min_idx = j
      newlist_p[min_idx] = newlist_p[i]
      newlist_p[i] = min_diffval

#Print the intervals in ascending order of size 
   for i in newlist_p:
      print (i)
 



main()