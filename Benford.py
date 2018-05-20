#  File: Benford.py

#  Description: Reads a file of population distribution, and prints a count (and relative frequency) of all instances of populations with first digits 1 through 9

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 21, 2016

#  Date Last Modified: April 21, 2016


def main():
  # create an empty dictionary pop_freq
   pop_freq = {}

  # initialize the dictionary
   pop_freq ["1"] = 0
  # fill the rest
   for i in range (2, 10):
      pop_freq ["%s" % i] = 0

  # open file for reading
   in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
   header = in_file.readline()
  
  # read subsequent lines
   for line in in_file:
      line = line.strip()
      pop_data = line.split()
    # get the last element that is the population number
      pop_num = pop_data[-1]
    # make entries in the dictionary
      for i in range (0, 10):
         if pop_num [0] == ("%s" % i):
            pop_freq ["%s" % i] += 1

  # create a variable sum_count to get a total sum of all counts in pop_freq
   sum_count = 0
   for i in range (1, 10):
       sum_count += (pop_freq ['%s' % i])

  # print the results for populations starting with digits 1 through 9
   print("Digit   Count   %")
   for i in range (1, 10):
      print (i, end = "       ")
      print("{0: <8}".format(pop_freq ['%s' % i]), end = "")
      print("%.1f" % (((pop_freq ['%s' % i])/sum_count * 100)))

  # close the file
   in_file.close()
  
main()