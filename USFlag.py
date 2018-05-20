#  File: USFlag.py
#  Description: Draw the United States flag in Turtle, using an input hoist in pixels
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: September 14, 2016
#  Date Last Modified: September 14, 2016


#Create a function "drawstar" to draw a solid white pentagram star given a radius and coordinates
def drawstar(ttl, radius, startx, starty):

#Approximate the length ("pentagon_length") of a side of a pentagon encompassing the star of given radius
   pentagon_length = radius * 2 * 0.587785
#Using that length, determine the length of each side of the pentagram star, assign to variable "st_len"
   st_len = pentagon_length / 1.618

#Assuming that the pen is already facing towards the right of the screen, begin drawing the solid white pentagram star
   ttl.goto(startx, starty)
   ttl.fillcolor("white")
   ttl.begin_fill()
   ttl.pendown()
   ttl.left(36)
   ttl.forward(st_len)
   ttl.right(72)
   ttl.forward(st_len)
   ttl.left(144)
   ttl.forward(st_len)
   ttl.right(72)
   ttl.forward(st_len)
   ttl.left(144)
   ttl.forward(st_len)
   ttl.right(72)
   ttl.forward(st_len)
   ttl.left(144)
   ttl.forward(st_len)
   ttl.right(72)
   ttl.forward(st_len)
   ttl.left(144)
   ttl.forward(st_len)
   ttl.right(72)
   ttl.forward(st_len)
   ttl.end_fill()
   ttl.penup()
   ttl.left(108)
   
   return

#Begin the main function
def main(): 

#Prompt the user to input the hoist of the flag in pixels, then import and initialize turtle using variable "ttl"
   Hi = eval(input("Enter vertical height (hoist) of the flag: "))
   while not Hi > 0:
      Hi = eval(input("Enter vertical height: "))
   else:
      import turtle 
      ttl = turtle.Turtle() 
      ttl.speed(10)

#Using the height "Hi", determine the width "Wid" and create a screen ("Flag") with 100 pixels in each margin
      Wid = 1.9 * Hi
      screen = turtle.Screen()
      screen.setup(200 + Wid,200 + Hi,0,0)
      screen.title ("Flag")    

#Draw the perimeter of the flag
   ttl.penup() 
   ttl.goto(-.5 * Wid,-.5 * Hi) 
   ttl.pendown() 
   ttl.forward(Wid)
   ttl.left(90)
   ttl.forward(Hi)
   ttl.left(90)
   ttl.forward(Wid)
   ttl.left(90)
   ttl.forward(Hi)
   ttl.left(90)
   ttl.penup()

#Start a for loop to draw each of the 7 red stripes in the flag
   for i in range(0, 7):
      ttl.pendown()
      ttl.fillcolor("red")
      ttl.begin_fill()
      ttl.forward(Wid)
      ttl.left(90)
      ttl.forward((1/13) * Hi)
      ttl.left(90)
      ttl.forward(Wid)
      ttl.left(90)
      ttl.forward((1/13) * Hi)
      ttl.left(90)
      ttl.penup()
      ttl.end_fill()
      ttl.left(90)
      ttl.forward((2/13) * Hi)
      ttl.right(90)

#Draw and fill the canton
   ttl.goto(-.5 * Wid,.5 * Hi)
   ttl.right(90)
   ttl.forward((7/13) * Hi)
   ttl.pendown()
   ttl.fillcolor("blue")
   ttl.begin_fill()
   ttl.left(90)
   ttl.forward((2/5) * Wid)
   ttl.left(90)
   ttl.forward((7/13) * Hi)
   ttl.left(90)
   ttl.forward((2/5) * Wid)
   ttl.left(90)
   ttl.forward((7/13) * Hi)
   ttl.left(90)
   ttl.penup()
   ttl.end_fill()

#Determine the radius of the stars in the flag
   radius = (Hi * 1 / 13) * (2 / 5)
#Using the radius, determine the length of one side of an encompassing pentagon
   pentagon_length = radius * 2 * 0.587785
#Using the radius, determine the length of a perpendicular line in an encompassing pentagon that stops at the center
   pyth_pent = radius * .809

#Initialize the coordinates (j,k) for 6 columns of 5 stars (30 stars)
   j = -(Wid / 2) + ((1 / 12) * (2/5) * (Wid)) - (pentagon_length/2)
   k = -(1/26 * Hi) + (1/10 * (7/13 * Hi)) - pyth_pent
   counter = 0
#Start a while loop to run until 30 stars have been drawn, moving the column and resetting the y-coordinate every 5 stars
   while counter < 30:
      drawstar(ttl,radius,j,k)
      counter += 1
      if counter !=0 and counter % 5 == 0:
         j += 2 * ((1 /12) * (2 / 5) * (Wid))
         k = -(1/26 * Hi) + (1/10 * (7/13 * Hi)) - pyth_pent
      else:
         k += 2 * ((1 / 10) * (7 / 13) * (Hi))

#Initialize the coordinates (j,k) for 5 columns of 4 stars (20 stars)
   j = -(Wid / 2) + 2*((1 / 12) * (2/5) * (Wid)) - (pentagon_length/2)
   k = -(1/26 * Hi) + 2*(1/10 * (7/13 * Hi)) - pyth_pent
   counter = 0
#Start a while loop to run until 20 stars have been drawn, moving the column and resetting the y-coordinate every 4 stars
   while counter < 20:
      drawstar(ttl,radius,j,k)
      counter += 1
      if counter !=0 and counter % 4 == 0:
         j += 2 * ((1 /12) * (2 / 5) * (Wid))
         k = -(1/26 * Hi) + 2*(1/10 * (7/13 * Hi)) - pyth_pent
      else:
         k += 2 * ((1 / 10) * (7 / 13) * (Hi))

   turtle.done() 

main() 