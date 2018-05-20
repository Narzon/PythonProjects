class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop(-1)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]

	def __str__(self):
		return str(self.items)
		if self.items == []:
			return "[]"


def main():

	Critical = Queue()
	Serious = Queue()
	Fair = Queue()

	ER = open("ERsim.txt", "r")
	instructions = ER.readlines()
	for line in instructions:
		line = line.strip().split()
		if line[0] == "exit":
			print(">>> Exit")
			return
		if line[0] == "add":
			if line[2] == "Critical":
				Critical.enqueue(str(line[1]))
				print(">>> Adding patient %s to Critical queue" % (str(line[1])))
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()
			if line[2] == "Serious":
				Serious.enqueue(str(line[1]))
				print(">>> Adding patient %s to Serious queue" % (str(line[1])))
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()
			if line[2] == "Fair":
				Fair.enqueue(str(line[1]))
				print(">>> Adding patient %s to Fair queue" % (str(line[1])))
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

		if line[0] == "treat":
			if line[1] == "next":
				print(">>> Treat next patient")
				print()
				if not Critical.isEmpty():
					print("Treating %s, from Critical queue" % (Critical.dequeue()))
				elif not Serious.isEmpty():
					print("Treating %s, from Serious queue" % (Serious.dequeue()))
				elif not Fair.isEmpty():
					print("Treating %s, from Fair queue" % (Fair.dequeue()))
				else:
					print("No patients in queues")
					print()
					continue	
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

			if line[1] == "Critical":
				print(">>> Treat next patient on Critical Queue")
				print()
				if not Critical.isEmpty():
					print("Treating %s, from Critical queue" % (Critical.dequeue()))
				else:
					print("No patients in queues")
					print()
					continue
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

			if line[1] == "Serious":
				print(">>> Treat next patient on Serious Queue")
				print()
				if not Serious.isEmpty():
					print("Treating %s, from Serious queue" % (Serious.dequeue()))
				else:
					print("No patients in queues")
					print()
					continue
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

			if line[1] == "Fair":
				print(">>> Treat next patient on Fair Queue")
				print()
				if not Fair.isEmpty():
					print("Treating %s, from Fair queue" % (Fair.dequeue()))
				else:
					print("No patients in queues")
					print()
					continue		
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

			if line[1] == "all":
				print(">>> Treat all patients")
				print()
				while not Critical.isEmpty() or not Serious.isEmpty() or not Fair.isEmpty():
					if not Critical.isEmpty():
						print("Treating %s, from Critical queue" % (Critical.dequeue()))
					elif not Serious.isEmpty():
						print("Treating %s, from Serious queue" % (Serious.dequeue()))
					elif not Fair.isEmpty():
						print("Treating %s, from Fair queue" % (Fair.dequeue()))
					print("Queues are:")
					print("Critical:",Critical)
					print("Serious:",Serious)
					print("Fair:",Fair)
					print()
				print("No patients in queue")
				print()


main()
