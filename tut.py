def drawstar(ttl, radius, startx, starty):

   pentagon_length = radius * 2 * 0.587785
   st_len = pentagon_length / 1.618
   st_ful = (pentagon_length / 2.618) + 2*(st_len)

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

def main(): 

   Hi = eval(input("Enter vertical height: "))
   while not Hi > 0:
      Hi = eval(input("Enter vertical height: "))
   else:
      import turtle 
      ttl = turtle.Turtle() 
      ttl.speed(10)
      Wid = 1.9 * Hi
      screen = turtle.Screen()
      screen.setup(200 + Wid,200 + Hi,0,0)
      screen.title ("Flag")    


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


   radius = (Hi * 1 / 13) * (2 / 5)
   pentagon_length = radius * 2 * 0.587785
   pyth_pent = radius * .809

   j = -(Wid / 2) + ((1 / 12) * (2/5) * (Wid)) - (pentagon_length/2)
   k = -(1/26 * Hi) + (1/10 * (7/13 * Hi)) - pyth_pent
   counter = 0
   while counter < 30:
      drawstar(ttl,radius,j,k)
      counter += 1
      if counter !=0 and counter % 5 == 0:
         j += 2 * ((1 /12) * (2 / 5) * (Wid))
         k = -(1/26 * Hi) + (1/10 * (7/13 * Hi)) - pyth_pent
      else:
         k += 2 * ((1 / 10) * (7 / 13) * (Hi))

   j = -(Wid / 2) + 2*((1 / 12) * (2/5) * (Wid)) - (pentagon_length/2)
   k = -(1/26 * Hi) + 2*(1/10 * (7/13 * Hi)) - pyth_pent
   counter = 0
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