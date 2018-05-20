#  File: htmlChecker.py
#  Description: Check an HTML text file to see if tags are correctly matched
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: October 5, 2016
#  Date Last Modified: October 6, 2016

#Define a Stack using a list, and define all appropriate methods
class Stack:
	def __init__(self):
		self.listitems = []
	def push(self, item):
		self.listitems.append(item)
	def pop(self):
		return self.listitems.pop()
	def peek(self):
		return self.listitems[-1]
	def size(self):
		return len(self.listitems)
	def isEmpty(self):
		return self.listitems == []

#Create a method "list" to return the Stack object in list form
	def list(self):
		return self.listitems

#Define a function "getTag" to search through a given text file at the current location character by character until finding a tag, denoted by angle brackets (or a whitespace). Return that tag.
def getTag(aFile):
	ch = "" 
	tag = ""
	while ch != "<":
		ch = aFile.read(1)
		if ch == "":
			return ""
	while ch != ">" and ch != " ":
		if ch == "<":
			ch = aFile.read(1)
		tag += ch
		ch = aFile.read(1)
		if ch == "":
			return ""
	return tag

#Define a function "getTaglist" to iterate through a given text file, and using function "getTag", return a list of every tag in the file
def getTaglist(aFile):
	tagList = []
	tag = getTag(aFile)
	while tag != "":
		tagList.append(tag)
		tag = getTag(aFile)
	return tagList

#Define a function "checkMatches", given a list of all tags in a file, to check for proper tag matching using Stack object "tagStack". Print every step of the iteration. Create and print a list of all valid tags, and check against a hard-coded list of exception tags.
def checkMatches(tagList):
	VALIDTAGS = []
	EXCEPTIONS = ["meta", "br", "hr"]
	tagStack = Stack()
	for item in tagList:
		if item[0] != "/":
			if item not in VALIDTAGS:
				VALIDTAGS.append(item)
				print ("Tag %s added to VALIDTAGS" % (item))
			if item in EXCEPTIONS:
				print("Tag %s does not need to match: stack is still" % (item), tagStack.list())
			else:
				tagStack.push(item)
				print ("Tag %s pushed: stack is now" % (item), tagStack.list())
		elif item[0] == "/":
			if item[1:] == tagStack.peek():
				print ("Tag %s matches top of stack: stack is now" % (item), tagStack.list())
				tagStack.pop()
			else:
				print ("Error: tag is %s but top of stack is %s" % (item, tagStack.peek()))
				return
	if tagStack.isEmpty():
		print ("Processing complete. No mismatches found.")
	else:
		print ("Processing complete. Unmatched tags remain on stack:", tagStack.list())
	print()
	print("List of VALIDTAGS:")
	print(sorted(VALIDTAGS))
	print()
	print("List of EXCEPTIONS:")
	print(sorted(EXCEPTIONS))

#Define the main function, to read the text file "htmlfile.txt", assign it to variable aFile, and then using function "getTaglist" assign variable "tagList" to a list of all tags in the file.
def main():
	aFile = open("htmlfile.txt", "r")
	tagList = getTaglist(aFile)
	print("List of all tags in file:")
	print()
	print(tagList)
	print()

#Use function "checkMatches" to iterate through the list for valid tag matching.
	checkMatches(tagList)


main()