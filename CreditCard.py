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
def is_valid(creditCard):

#Create a list (list_n) with each digit from the credit card number in backwards order
   list_n = []
   for i in range (0, 16):
      list_digit = creditCard % 10
      list_n.append(list_digit)
      creditCard = creditCard // 10

#Going through the list, multiply each "odd" digit (index 1, 3, 5, etc) by 2 and sum its digits using sum_digits
   for i in range (1, 16, 2):
      list_n[i] = list_n[i] * 2
      list_n[i] = sum_digits(list_n[i])

#If the sum of all digits in the list is divisible by 10, return True. Otherwise, return False
   if int(sum(list_n)) % 10 == 0:
      return True
   else:
      return False

#Create the function cc_type so that given a credit card number it will return what (if any) type of credit card the number belongs to. Otherwise, return an empty string
def cc_type(creditCard):

#Convert the credit card number to a string. Checking the string index numbers at the beginning of a given credit card number string, return the appropriate credit card type (AmEx, Discover, Mastercard, or Visa)
   cred_str = str(creditCard)
   if cred_str[0] == "3":
      if cred_str[1] == "4" or cred_str[1] == "7":
         return " American Express"
      else:
         return ""
   if cred_str[0] == "6":
      if cred_str[1:4] == "011" or cred_str[1:3] == "44" or cred_str[1] == "5":
         return " Discover"
      else:
         return ""
   if cred_str[0:2] == "50" or cred_str[0:2] == "51" or cred_str[0:2] == "52" or cred_str[0:2] == "53" or cred_str[0:2] == "54" or cred_str[0:2] == "55":
      return " MasterCard"
   if cred_str[0] == "4":
      return " Visa"
   else:
      return ""

#Create the main function
def main():

#Prompt the user to input a number. Assign the variable credit_num to keep track of the number as an integer
   creditCard = eval(input("Enter 15 or 16-digit credit card number: "))

#Print a space for formatting
   print()

#Print an error message and exit the program if the given number is not 15 or 16 digits
   if len(str(creditCard)) != 15 and len(str(creditCard)) != 16:
      print("Not a 15 or 16-digit number")
      return

#Create the variable type_card using the cc_type function defined above to assign what type of credit card (if any) the number belongs to
   type_card = cc_type(creditCard)

#Using the function is_valid defined above, determine if the number is a valid CC number. If so, print that it is valid along with the type of card it belongs to
   if is_valid(creditCard):
      print("Valid%s credit card number" % type_card)

#If the number is not valid, print that as the result
   else:
      print("Invalid credit card number")
main()