#  File: ISBN.py

#  Description: Open a file of ISBNs and write to a different file whether they are valid or invalid ISBNs 

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 2, 2016

#  Date Last Modified: April 2, 2016

import string

#Create a function to check if an ISBN (st) is valid

def is_valid(st):

#Remove any hyphens from the ISBN
   st = st.replace("-","")

#Check to make sure the length of the ISBN is 10, and that the first 9 characters are digits
   if len(st) == 10 and st[0:9].isdigit():

#Check to make sure the last character is either a digit, or an X (independent of case)
      if st[9] == "X" or st[9] == "x" or st[9].isdigit():

#Create a new list newSt and copy over the first 9 digits. If the 10th is an X, append the integer 10. Otherwise, append the last digit.
         newSt = []
         for j in range(0, 9):
            newSt.append(int(st[j]))
         if st[9] == "X" or st[9] == "x":
            newSt.append(int(10))
         else:
            newSt.append(int(st[9]))
         
#Get the partial sum for the new list twice
         for i in range (1, 10):
            newSt[i] = int(newSt[i - 1]) + int(newSt[i])
         for i in range (1, 10):
            newSt[i] = int(newSt[i - 1]) + int(newSt[i])

#Check to see if the last digit is divisible by 11. If so, return True. If any conditions aren't met, return False.
         if int(newSt[9]) % 11 == 0:
            return True
         else:
            return False
      else:
         return False
   else:
      return False



def main():

#Open the file isbn.txt in read mode and assign it to variable isbn 
   isbn = open("isbn.txt", "r")

#Create a new variable readisbn to use the information in isbn.txt
   readisbn = isbn

#Open the file isbnOut.txt in write mode and assign it to variable isbncheck
   isbncheck = open("isbnOut.txt", "w")

#For each line in readisbn, save the original format of the ISBN to original_line
   for line in readisbn:      
      readisbn = line.strip("\n")
      original_line = str(readisbn)

#Use the function is_valid to determine whether the ISBN is valid or invalid.
      if is_valid(readisbn):
         status = " valid \n"
      else:
         status = " invalid \n"

#Write a new line to isbncheck, with the original ISBN and the validity status.
      writtenline = ("%s %s" % (original_line, status))
      isbncheck.write(writtenline)

#Close both files
   isbn.close()
   isbncheck.close()
main()

