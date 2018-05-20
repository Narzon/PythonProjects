#  File: ExpressionTree.py
#  Description: Create trees to solve arithmetic expressions from a text file by traversing the trees in infix, prefix, and postfix notations
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: December 1, 2016
#  Date Last Modified: December 1, 2016

#Create a function to check if a string could represent an integer
def is_int(n):
	if n.isdigit():
		return True
	else:
		return False
#Create a function to check if a string could represent a float but not an integer
def is_float(n):
   if n.isdigit():
   	return False
   try:
      float(n)
      return True
   except ValueError:
      return False

#Create a Binary Tree class, including standard methods
class BinaryTree (object):
	  
	def __init__ (self, treeVal):
		self.data = treeVal
		self.left = None
		self.right = None
		
#Define a method to create a tree given an expression string expr, going through each element of the expression
	def createTree (self, expr):
#Define variable self.pointer to keep track of "current" nodes
		self.pointer = self
#Define a stack treeStack to keep track of previous pointer locations
		self.treeStack = Stack()
		self.tokens = expr.split()
		for i in self.tokens:

#if an element is "(", create a new left node from the current and point to that node
			if i == "(":
				self.pointer.insertLeft(None)
				self.treeStack.push(self.pointer)
				self.pointer = self.pointer.left
#If an element is an operand, set the current value to that number and point to the parent node				
			if is_int(i):
				self.pointer.setRootVal(int(i))
				self.pointer = self.treeStack.pop()

			if is_float(i):
				self.pointer.setRootVal(float(i))
				self.pointer = self.treeStack.pop()
#If an element is an operator, set the current value to that operator, create a new right node, and point to that node
			if i in ("+","-","/","*"):
				self.pointer.setRootVal(i)
				self.pointer.insertRight(None)
				self.treeStack.push(self.pointer)
				self.pointer = self.pointer.right
#If an element is ")" and is not the final element of the expression, point to the parent node 
			if i == ")":
				if not self.treeStack.isEmpty():
					self.pointer = self.treeStack.pop()

#Define a method evaluate to recursively traverse the tree in an infix order, evaluating the expression
	def evaluate (self, root):

		if root.data == "+":
			return self.evaluate(root.left) + self.evaluate(root.right)
		if root.data == "*":
			return self.evaluate(root.left) * self.evaluate(root.right)
		if root.data == "/":
			return self.evaluate(root.left) / self.evaluate(root.right)
		if root.data == "-":
			return self.evaluate(root.left) - self.evaluate(root.right)
		if root.data != None:
			return root.data

#Define a method preOrder to print the expression in prefix notation
	def preOrder (self, root):
		if root != None:
			print("%s " % (root.getRootVal()), end = "")
			self.preOrder(root.getLeftChild())
			self.preOrder(root.getRightChild())

#Define a method postOrder to print the expression in postfix notation
	def postOrder (self, root):
		if root != None:
			self.postOrder(root.getLeftChild())
			self.postOrder(root.getRightChild())
			print("%s " % (root.getRootVal()), end = "")

	def getLeftChild (self):
		return self.left

	def getRightChild (self):
		return self.right

	def setRootVal (self,val):
		self.data = val

	def getRootVal (self):
		return self.data

	def insertLeft (self,newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.left = self.left
			self.left = t

	def insertRight (self,newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.right = self.right
			self.right = t

#Define a regular Stack class
class Stack (object):
	def __init__(self):
		self.items = [ ]

	def isEmpty (self):
		return self.items == [ ]

	def push (self, item):
		self.items.append (item)

	def pop (self):
		return self.items.pop ()

	def peek (self):
		return self.items [len(self.items)-1]

	def size (self):
		return len(self.items)


def main():

#Open the text file treedata.txt, and for each line create a new tree for the arithmetic expression
	treeData = open("treedata.txt", "r")

	for line in treeData:
		newTree = BinaryTree(None)
		line = line.strip()
		newTree.createTree(line)
		print("Infix expression: ", line)
		print()
#Use evaluate to solve the expression
		print("   Value:  ", newTree.evaluate(newTree))
		print("   Prefix Expression:   ", end = "")
#Print the prefix notation
		newTree.preOrder(newTree)
		print("")
		print("   Postfix Expression:   ", end = "")
#Print the postfix notation
		newTree.postOrder(newTree)
		print()
		print()
#Read the next line
		line = treeData.readline()		


main()