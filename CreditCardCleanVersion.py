#  File: CreditCard.py

#  Description: Given a 15 or 16-digit number, print whether or not the number is a valid credit card number, and if applicable what type of credit card it is

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 7, 2016

#  Date Last Modified: April 7, 2016

#Create the function sum_digits to add all digits in a given number together
def sum_digits(n):
   n = int(n)
   sum_num = 0
   while (n > 0):
      sum_num = sum_num + (n % 10)
      n = n // 10
   return sum_num

#Create the function is_valid to determine whether a given 15 or 16-digit number is a valid CC number
def is_valid(n):

#Create the variable list_n as an empty list, and assign the credit card number given as a string to variable string_n
   list_n = []
   string_n = str(n)

#Using the string variable string_n, add each digit as an integer to list_n
   for i in string_n:
      list_n.append(int(i))

#Starting at the end of the list (in the format ...d5 d4 d3 d2 d1 d0), go through each integer and if it is "odd" (d1, d3, etc.), double it and then use the above function sum_digits to add all digits
   for i in range (2, len(list_n) + 1, 2):
      list_n[-i] = list_n[-i] * 2
      list_n[-i] = sum_digits(list_n[-i])

#If the sum of all digits in the list is divisible by 10, return True. Otherwise, return False.
   if int(sum(list_n)) % 10 == 0:
      return True
   else:
      return False

#Create the function cc_type so that given a credit card number, the function will return what (if any) type of credit card the number belongs to. Otherwise, return an empty string
def cc_type(cred_num):

#checking the string index numbers at the beginning of a given credit card number string, return the appropriate credit card type (AmEx, Discover, Mastercard, or Visa)
   cred_str = str(cred_num)
   if cred_str[0] == "3":
      if cred_str[1] == "4" or cred_str[1] == "7":
         return "American Express"
      else:
         return ""
   if cred_str[0] == "6":
      if cred_str[1:4] == "011" or cred_str[1:3] == "44" or cred_str[1] == "5":
         return "Discover"
      else:
         return ""
   if cred_str[0:2] == "50" or cred_str[0:2] == "51" or cred_str[0:2] == "52" or cred_str[0:2] == "53" or cred_str[0:2] == "54" or cred_str[0:2] == "55":
      return "MasterCard"
   if cred_str[0] == "4":
      return "Visa"
   else:
      return ""

#Create the main function
def main():

#Prompt the user to input a number. Assign the variable credit_num to keep track of the number as an integer
   credit_num = eval(input("Enter 15 or 16-digit credit card number: "))
   credit_num = int(credit_num)

#Print a space for formatting
   print()

#Create the variable type_card using the cc_type function defined above to assign what type of credit card (if any) the number belongs to
   type_card = cc_type(credit_num)

#Print an error message if the given number is not 15 or 16 digits
   if len(str(credit_num)) != 15 and len(str(credit_num)) != 16:
      print("Not a 15 or 16-digit number")
      return

#Using the function is_valid defined above, determine if the number is a valid CC number. If so, print that it is valid along with the type of card it belongs to
   else:
      if is_valid(credit_num):
         print("Valid %s credit card number" % type_card)

#If the number is not valid, print that as the result
      else:
         print("Invalid credit card number")
         
main()