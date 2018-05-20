#  File: Day.py

#  Description: This program computes the day of the week for a given date.

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: January 31, 2016

#  Date Last Modified: January 31, 2016

def main():
# Prompt user to enter year, if it's more than 2100 or less than 1900 keep asking
   year = eval(input("Enter year: "))
   while year > 2100:
      year = eval(input("Enter year: "))
   while year < 1900:
      year = eval(input("Enter year: "))

# Prompt user to enter month, if it's more than 12 or less than 1 keep asking
   month = eval(input("Enter month: "))
   while month > 12:
      month = eval(input("Enter month: "))
   while month < 1:
      month = eval(input("Enter month: "))

# Prompt user for day of the month, if it's not the correct number of days for that month/year keep asking
   day = eval(input("Enter day: "))
   if month == 1:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))


# Check February for leap year; if the year is divisible by 4 and is not 1900 or 2100, allow 29 days
   if month == 2:
      if year % 4 == 0 and year != 1900 and year != 2100:
         while day > 29:
            day = eval(input("Enter day: "))
         while day < 1:
            day = eval(input("Enter day: "))
      else:
         while day > 28:
            day = eval(input("Enter day: "))
         while day < 1:
            day = eval(input("Enter day: "))


   if month == 3:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 4:
      while day > 30:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 5:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 6:
      while day > 30:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 7:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 8:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 9:
      while day > 30:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 10:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 11:
      while day > 30:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))
   if month == 12:
      while day > 31:
         day = eval(input("Enter day: "))
      while day < 1:
         day = eval(input("Enter day: "))

# Assign variable a for month
# Make sure that for variable a, months start from March (so March = 1 and February = 12)
   if month == 1:
      a = 11
   if month == 2:
      a = 12
   if month == 3:
      a = 1
   if month == 4:
      a = 2
   if month == 5:
      a = 3
   if month == 6:
      a = 4
   if month == 7:
      a = 5
   if month == 8:
      a = 6
   if month == 9:
      a = 7
   if month == 10:
      a = 8
   if month == 11:
      a = 9
   if month == 12:
      a = 10

# Assign variable b for day
   b = day

# Make sure years follow the new month scheme (so input January 2009 gives month = 11 and year = 2008)
   if month == 1:
      fixedyear = (year - 1)
   elif month == 2:
      fixedyear = (year - 1)
   else:
      fixedyear = year 

# Strip century from year to get year of that century, assign variable c
   if fixedyear > 1900 and fixedyear < 2000:
      c = fixedyear - 1900
   elif fixedyear > 2000 and fixedyear < 2100:
      c = fixedyear - 2000
   elif fixedyear == 1900 or fixedyear == 2000 or fixedyear == 2100:
      c = 0

# Strip year of century from year to get century (19 for 1900, 20 for 2000, 21 for 2100 etc)
   if fixedyear // 2100 == 1:
      d = 21
   elif fixedyear // 2000 == 1:
      d = 20
   elif fixedyear // 1900 == 1:
      d = 19

# Use variables to compute given algorithm
   w = (13 * a - 1 ) // 5 
   x = c // 4 
   y = d // 4 
   z = w + x + y + b + c - 2 * d 
   r = z % 7 
   r = (r + 7) % 7

# Assign variable r to appropriate day of the week
   if r == 0:
      dayofweek = "Sunday."
   if r == 1:
      dayofweek = "Monday."
   if r == 2:
      dayofweek = "Tuesday."
   if r == 3:
      dayofweek = "Wednesday."
   if r == 4:
      dayofweek = "Thursday."
   if r == 5:
      dayofweek = "Friday."
   if r == 6:
      dayofweek = "Saturday."

# print result
   print ("The day is",dayofweek) 

main()