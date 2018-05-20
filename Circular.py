#  File: Circular.py
#  Description: Create a circular linked list ADT to play through games of Hot Potato
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: October 28, 2016
#  Date Last Modified: October 28, 2016


#Define a class Node using conventional methods
class Node (object):

   def __init__(self,initdata):
      self.data = initdata
      self.next = None         
                                  
   def getData (self):
      return self.data            

   def getNext (self):
      return self.next            

   def setData (self, newData):
      self.data = newData         

   def setNext (self,newNext):
      self.next = newNext         

#Define a CircularList, as a modified linked list with special methods
class CircularList(object):

#Upon creating a CircularList, define a sentinel node for the head
   def __init__(self):
      self.head = Node("sentinel")
      self.head.setNext(None)

#Define the method "add" to place a new item as a node at the end of the CircularList
   def add (self,item):
      current = self.head.getNext()
      #if the list is empty, point the sentinel to this new node, and point the new node to the sentinel's pointer
      if current != None:
         while current.getNext() != self.head.getNext():
            current = current.getNext()
         temp = Node(item)
         current.setNext(temp)
         current.getNext().setNext(self.head.getNext())
      #if the list isn't empty, add normally
      else:
         temp = Node(item)
         self.head.setNext(temp)
         temp.setNext(self.head.getNext())      

   def isEmpty (self):
      return self.head.getNext() == None

#Define the method onlyOneNode  
   def onlyOneNode (self):
      #if the CircularList is empty, return False
      if self.head.getNext() == None:
         return False
      #if the sentinel and the item it points to share pointers, return True
      current = self.head.getNext()
      if self.head.getNext() == current.getNext():
         return True
      else:
         return False

#Define the method remove, given a current and previous pointer
   def remove (self,current,previous):
      #if current is the first item on the CircularList, make sure remaining items deal with the sentinel node correctly
      if self.head.getNext() == current:
         self.head.setNext(current.getNext())
         previous.setNext(self.head.getNext())
         current = current.getNext()
         #return the new current as the item that followed the removed item
         return current
      #else, remove normally
      else:   
         previous.setNext(current.getNext())
         current = current.getNext()
         return current

#Define a method playGame given a number of iterations n
   def playGame (self, n):
      print("New game of Hot Potato!")
      print("Number of iterations per round of Hot Potato:", n)
      print("Players in this game:")
      print()
      print(self.__str__())
      print()
      #define a counter to keep track of how many rounds are played per game
      counter = 0
      #point current to the first item on the CircularList
      current = self.head.getNext()
      previous = None
      #set a loop to run until only one item remains in the CircularList
      while not self.onlyOneNode():   
         iterations = n
         while iterations > 1:
            iterations -= 1
            previous = current
            current = current.getNext()
         elimPerson = current.getData()
         counter += 1
         #use the method remove for each iteration
         current = self.remove(current,previous)
         print("Iteration: %s" % (counter))
         print("%s is eliminated in this round!" % (elimPerson))
         print("Players remaining:")
         print()
         print(self.__str__())
         print()
      #if only one item remains, print the winner
      if self.onlyOneNode():
         print("The sole survivor is: %s" % (current.getData()))
         print()
         print()

#Define a __str__ method to return the CircularList as a string, with a new line every 10 items
   def __str__(self):
      if self.isEmpty():
         return ""
      linkstr = ""
      current = self.head.getNext()
      linkstr += str(current.getData())
      if current.getNext() == self.head.getNext():
         return linkstr
      else:
         current = current.getNext()
         counter = 0
         while current.getNext() != self.head.getNext():
            if counter == 9:
               linkstr += ","
               linkstr += "\n"
               counter = -1
            else:
               linkstr += ", "
            linkstr += str(current.getData())
            current = current.getNext()
            counter += 1
         if counter == 9:
            linkstr += ","
            linkstr += "\n"
            linkstr += str(current.getData())
         else:
            linkstr += ", "
            linkstr += str(current.getData())
         return linkstr

#Define the main function
def main():

   #open the data file HotPotatoData.txt as variable hotPot
   hotPot = open("HotPotatoData.txt", "r")

   #read the first line
   line = hotPot.readline()
   #run a loop until reaching a blank line (representing the end of the data sets)
   while line != "":
      #for each loop iteration, create a CircularList, hotList
      hotList = CircularList()
      #for the first line of each data set, extract the values for the iterations and the number of players per game
      line = line.strip().split()
      n = int(line[1])
      #using the number of players given, read each player line and add them to hotList
      for i in range(int(line[0])):
         hotList.add(hotPot.readline().strip())
      #once all players have been added, run a game of Hot Potato using the function platGame and the number n of iterations
      hotList.playGame(n)
      #read the next line
      line = hotPot.readline()


main()