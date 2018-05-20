#  File: EasterSunday.py

#  Description: This program computes the date of Easter Sunday for a given year.

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: January 30, 2016

#  Date Last Modified: January 30, 2016

def main():
# Prompt user to enter year
   year = eval(input("Enter year: "))

# Define year as y
   y = year

# Compute algorithm
   a = y % 19
   b = y // 100
   c = y % 100
   d = b // 4
   e = b % 4
   g = (8 * b + 13)  // 25
   h = (19 * a + b - d - g + 15) % 30
   j = c // 4
   k = c % 4
   m = (a + 11 * h) // 319
   r = (2* e + 2 * j - k - h + m + 32) % 7
   n = (h - m + r + 90) // 25
   p = (h - m + r + n + 19) % 32
   
# define months by name of month
   if n == 1:
      month = "January."
   elif n == 2:
      month = "February."
   elif n == 3:
      month = "March."
   elif n == 4:
      month = "April."
   elif n == 5:
      month = "May."
   elif n == 6:
      month = "June."
   elif n == 7:
      month = "July."
   elif n == 8:
      month = "August."
   elif n == 9:
      month = "September."
   elif n == 10:
      month = "October."
   elif n == 11:
      month = "November."
   elif n == 12:
      month = "December."

# print result
   print ("In",year,"Easter Sunday is on",p,month) 

main()