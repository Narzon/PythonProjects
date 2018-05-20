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


class Stack (object):
   def __init__(self):
      sentinel = Node(None)
      self.head = sentinel
   def isEmpty(self):
      if self.head.getNext() == None:
         return True
      else:
         return False
   def push(self, item):
      temp = Node(item)
      if self.head.getNext() == None:
         self.head.setNext(temp)
      else:
         temp.setNext(self.head.getNext())
         self.head.setNext(temp)
   def pop(self):
      old = self.head.getNext().getData()
      self.head.setNext(self.head.getNext().getNext())
      return old
   def peek(self):
      return self.head.getNext().getData()
   def size(self):
      if self.isEmpty():
         return 0
      else:
         current = self.head.getNext()
         count = 1
         while current.getNext() != None:
            count += 1
            current = current.getNext()
         return count

class Queue (object):
   def __init__(self):
      sentinel = Node(None)
      self.head = sentinel
   def isEmpty(self):
      if self.head.getNext() == None:
         return True
      else:
         return False
   def enqueue(self, item):
      if self.isEmpty():
         temp = Node(item)
         self.head.setNext(temp)
      else:
         temp = Node(item)
         current = self.head.getNext()
         while current.getNext() != None:
            current = current.getNext()
         current.setNext(temp)
   def dequeue(self):
      if self.isEmpty():
         return None
      old = self.head.getNext()
      self.head.setNext(self.head.getNext().getNext())
      return old.getData()
   def size(self):
      if self.isEmpty():
         return 0
      else:
         current = self.head.getNext()
         count = 1
         while current.getNext() != None:
            count += 1
            current = current.getNext()
         return count
   def peek(self):
      if self.isEmpty():
         return None
      return self.head.getNext().getData()

class Dequeue(object):
   def __init__(self):
      self.head = Node("sentinel")
      self.head.setNext(None)
   def isEmpty(self):
      if self.head.getNext() == None:
         return True
      else:
         return False
   def size(self):
      if self.isEmpty():
         return 0
      else:
         current = self.head.getNext()
         count = 1
         while current.getNext() != None:
            count += 1
            current = current.getNext()
         return count
   def addRear(self,item):
      temp = Node(item)
      if self.isEmpty():
         self.head.setNext(temp)
      current = self.head.getNext()
      while current.getNext() != None:
         current = current.getNext()
      current.setNext(temp)
   def removeRear(self):
      if self.isEmpty():
         return "Nothing to remove"
      current = self.head.getNext()
      while current.getNext().getNext() != None:
         current = current.getNext()
      old = current.getNext().getData()
      current.setNext(None)
      return old
   def addFront(self,item):
      temp = Node(item)
      if self.isEmpty():
         self.head.setNext(temp)
      else:
         temp.setNext(self.head.getNext())
         self.head.setNext(temp)
   def removeFront(self):
      if self.isEmpty():
         return "Nothing to remove"
      else:
         old = self.head.getNext().getData()
         self.head.setNext(self.head.getNext().getNext())
         return old

def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string

def calculatePref(prefix):
   stack = Stack()
   prefix = prefix.split()
   new_prefix = []
   for i in prefix[::-1]:
      new_prefix.append(i)


   for i in new_prefix:

      if i == "+":
         summ = int(stack.pop()) + int(stack.pop())
         stack.push(str(summ))

      elif i == "-":
         dif = int(stack.pop()) - int(stack.pop())
         stack.push(str(dif))

      elif i == "*":
         prod = int(stack.pop()) * int(stack.pop())
         stack.push(str(prod))

      elif i == "/":
         quo = int(stack.pop()) // int(stack.pop())
         stack.push(str(quo))

      elif i !=  " ":
         stack.push(i)

   return stack.pop()

def sumofStack(stack):
   oldSum = 0
   if stack.isEmpty():
      return 0
   else:
      oldSum += stack.pop() + sumofStack(stack)
      stack.push(oldSum)
      return oldSum





def main():
   print("Making a Queue. Should read True, False, 3, Cat, Cat, 2")
   queue = Queue()
   print(queue.isEmpty())
   queue.enqueue("Cat")
   queue.enqueue("Dog")
   queue.enqueue("Bird")
   print(queue.isEmpty())
   print(queue.size())
   print(queue.peek())
   print(queue.dequeue())
   print(queue.size())

   print()
   print("Making a Dequeue. Should read True, 3, False, Cat, Dog, 1")
   d = Dequeue()
   print(d.isEmpty())
   d.addFront("bear")
   d.addFront("cat")
   d.addRear("dog")
   print(d.size())
   print(d.isEmpty())
   print(d.removeFront())
   print(d.removeRear())
   print(d.size())

   print()
   print("Print the result of prefix notation")
   print(calculatePref("+ * + 3 6 - 2 4 7"))

   print()
   print("Sum elements of a stack of 1, 2, 3, 4, 5")
   sumStack = Stack()
   sumStack.push(1)
   sumStack.push(2)
   sumStack.push(3)
   sumStack.push(4)
   sumStack.push(5)
   print(sumofStack(sumStack))

main()

         

