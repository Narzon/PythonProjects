
def main():
  # create an empty dictionary
   pop_freq = {}

  # initialize the dictionary
   pop_freq ['1'] = 0
  # fill the rest
   for i in range (2, 9):
      pop_freq ['%s' % i] = 0
   pop_freq ['9'] = 0

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
         if pop_num[0] == ('%s' % i):
            pop_freq ['%s' % i] += 1

   sum_count = 0
   for i in range (1, 10):
       sum_count += (pop_freq ['%s' % i])

   print("Digit   Count   %")
   for i in range (1, 10):
      print (i, end = "       ")
      print("{0: <4}".format(pop_freq ['%s' % i]), end = "    ")
      print("%.1f" % (((pop_freq ['%s' % i])/sum_count * 100)))







  # close the file
   in_file.close()

  # write out the result

  
main()