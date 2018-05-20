#  File: LinkedLists.py
#  Description: Define a class for a generic LinkedList with class methods for specified utilities
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: October 20, 2016
#  Date Last Modified: October 20, 2016

#Define a class Node with usual methods to be used in LinkedList
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

#Define a class LinkedList with a sentinel node
class LinkedList ():
   def __init__(self):
      self.head = Node("sentinel")
      self.head.setNext(None)

#Define the method isEmpty to check if there are any data nodes in the list
   def isEmpty (self):
      return self.head.getNext() == None

#Define a __str__ method to return a string of all data in the linked list, formatted properly (surrounded by square brackets, spaces every 2 lines, new line every 10 items)
   def __str__(self):
      if self.isEmpty():
         return "[]"
      linkstr = "["
      current = self.head.getNext()
      linkstr += str(current.getData())
      current = current.getNext()
      counter = 0
      while current != None:
         if counter == 9:
            linkstr += "\n" + " "
            counter = -1
         else:
            linkstr += " "
         linkstr += str(current.getData())
         current = current.getNext()
         counter += 1
      linkstr += "]"
      return linkstr

#Define method addFirst to add a new item to the beginning of the LinkedList
   def addFirst (self, item):
      temp = Node(item)
      temp.setNext(self.head.getNext())
      self.head.setNext(temp)

#Define method addLast to add a new item to the end of the LinkedList
   def addLast (self,item):
      current = self.head.getNext()
      previous = self.head

      while current != None:
            previous = current
            current = current.getNext()

      temp = Node(item)
      temp.setNext(current)
      previous.setNext(temp)

#Define method addInOrder to add a new item in proper ascending order to the LinkedList
   def addInOrder (self,item):
      current = self.head.getNext()
      previous = self.head
      stop = False

      while current != None and not stop:
         if current.getData() > item:
            stop = True
         else:
            previous = current
            current = current.getNext()

      temp = Node(item)
      temp.setNext(current)
      previous.setNext(temp)

#Define a method to return the length (number of data nodes) of a LinkedList
   def getLength (self):
      current = self.head.getNext()
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

#Define a method findUnordered to search for an item in an unordered list. Return True if found, else False
   def findUnordered (self, item): 
      current = self.head.getNext()
      inList = False
      while current != None and not inList:
         if current.getData() == item:
            inList = True
         current = current.getNext()

      return inList

#Define a method findOrdered to search for an item in an ordered list, stopping the search loop early if a greater value item is found.
   def findOrdered (self, item):
      current = self.head.getNext()
      previous = self.head
      stop = False
      inList = False

      while current != None and not stop and not inList:
         if current.getData() > item:
            stop = True
         if current.getData() == item:
            inList = True
         current = current.getNext()

      return inList

#Define a method delete to remove an item from an unordered list
   def delete (self,item):
      current = self.head.getNext()
      previous = self.head
      found = False

      while not found and current != None:
         if current.getData() == item:
            found = True
            previous.setNext(current.getNext())
         else:
            previous = current
            current = current.getNext()

      return found

#Define a method copyList to return a new list with the nodes and items as the original
   def copyList (self):
      copyList = LinkedList()

      current = self.head.getNext()
      while current != None:
         copyList.addLast(current.getData())
         current = current.getNext()

      return copyList

#Define a method reverseList to return a new list with the same items as the original in reversed order
   def reverseList (self):
      reverseList = LinkedList()

      current = self.head.getNext()
      while current != None:
         reverseList.addFirst(current.getData())
         current = current.getNext()

      return reverseList

#Define a method orderList to return a new list with the same items as the original in ascending order
   def orderList (self): 
      orderList = LinkedList()

      current = self.head.getNext()
      while current != None:
         orderList.addInOrder(current.getData())
         current = current.getNext()

      return orderList

#Define a method isOrdered, comparing a copy of a list to an ordered copy to determine if the list is already ordered
   def isOrdered (self):
      return str(self.copyList()) == str(self.orderList())

#Define a method mergeList to combine the elements of two given LinkedLists and return them as a new ordered LinkedList
   def mergeList (self, b):      
      newCopy = self.copyList()

      current = b.head.getNext()
      while current != None:
         newCopy.addInOrder(current.getData())
         current = current.getNext()

      return newCopy

#Define a method isEqual to determine if two given lists have the same elements, going node by node
   def isEqual (self, b):
      if self.getLength() != b.getLength():
         return False

      bothEqual = True
      current = self.head.getNext()
      currentb = b.head.getNext()
      while current != None:
         if current.getData() != currentb.getData():
            bothEqual = False
         current = current.getNext()
         currentb = currentb.getNext()

      return bothEqual

#Define a method to search a LinkedList, comparing to tempList for duplicate items. Remove duplicate items every subsequent time they appear
   def removeDuplicates (self):
      removeCopy = self.copyList()
      current = removeCopy.head.getNext()
      previous = None
      tempList = []
      while current != None:
         if current.getData() in tempList:
            previous.setNext(current.getNext())
            current = current.getNext()
         else:
            tempList.append(current.getData())
            previous = current
            current = current.getNext()

      return removeCopy








#Run the given main function
def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()