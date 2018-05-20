

#def is_number(n):
#	 try:
#		  float(n)
#		  return True
#	 except ValueError:
#		  return False

def is_int(n):
	if n.isdigit():
		return True
	else:
		return False

def is_float(n):
   if n.isdigit():
   	return False
   try:
      float(n)
      return True
   except ValueError:
      return False


class BinaryTree (object):
	  
	def __init__ (self, treeVal):
		self.data = treeVal
		self.left = None
		self.right = None
		

	def createTree (self, expr):
		self.pointer = self
		self.treeStack = Stack()
		self.tokens = expr.split()
		for i in self.tokens:
			
			if i == "(":
				self.pointer.insertLeft(None)
				self.treeStack.push(self.pointer)
				self.pointer = self.pointer.left
				
			if is_int(i):
				self.pointer.setRootVal(int(i))
				self.pointer = self.treeStack.pop()

			if is_float(i):
				self.pointer.setRootVal(float(i))
				self.pointer = self.treeStack.pop()

			if i in ("+","-","/","*"):
				self.pointer.setRootVal(i)
				self.pointer.insertRight(None)
				self.treeStack.push(self.pointer)
				self.pointer = self.pointer.right
				
			if i == ")":
				if not self.treeStack.isEmpty():
					self.pointer = self.treeStack.pop()

	
	def dumpTree(self):
		if self.left != None:
			print ("left child of ",self.data,":",self.left.data)
			self.left.dumpTree()
		if self.right != None:
			print ("right child of ",self.data,":",self.right.data)
			self.right.dumpTree()


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


	def preOrder (self, root):
		if root != None:
			print("%s " % (root.getRootVal()), end = "")
			self.preOrder(root.getLeftChild())
			self.preOrder(root.getRightChild())

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
	treeData = open("treedata.txt", "r")
	

	for line in treeData:
		newTree = BinaryTree(None)
		line = line.strip()
		newTree.createTree(line)
		print("Infix expression: ", line)
		print()
		print("   Value:  ", newTree.evaluate(newTree))
		print("   Prefix Expression:   ", end = "")
		newTree.preOrder(newTree)
		print("")
		print("   Postfix Expression:   ", end = "")
		newTree.postOrder(newTree)
		print()
		print()
		line = treeData.readline()		


main()