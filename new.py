
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
	def list(self):
		return self.listitems

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

def getTaglist(aFile):
	tagList = []
	tag = getTag(aFile)
	while tag != "":
		tagList.append(tag)
		tag = getTag(aFile)
	return tagList

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
				print()
				print("List of VALIDTAGS:")
				print(VALIDTAGS)
				print()
				print("List of EXCEPTIONS:")
				print(EXCEPTIONS)
				return
	if tagStack.isEmpty():
		print ("Processing complete. No mismatches found.")
	else:
		print ("Processing complete. Unmatched tags remain on stack:", tagStack.list())
	print()
	print("List of VALIDTAGS:")
	print(VALIDTAGS)
	print()
	print("List of EXCEPTIONS:")
	print(EXCEPTIONS)


def main():
	aFile = open("htmlfile.txt", "r")
	tagList = getTaglist(aFile)
	print("List of all tags in file:")
	print()
	print(tagList)
	print()
	checkMatches(tagList)


main()