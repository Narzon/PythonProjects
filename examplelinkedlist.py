class UnorderedList (object):

   def __init__(self):
      sentinel = Node(None)
      self.head = sentinel

   def isEmpty (self):
      return self.head.getNext() == None


   def add (self,item):

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
      
   def length (self):
      current = self.head.getNext()
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def search (self,item):
      current = self.head.getNext()
      found = False

      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found

   def remove (self,item):
      current = self.head.getNext()
      previous = self.head
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      previous.setNext(current.getNext() )