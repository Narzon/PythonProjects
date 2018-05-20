#  File: ERsim.py
#  Description: Run through a simulation of an ER with queues for Critical, Serious, and Fair condition patients
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: October 12, 2016
#  Date Last Modified: October 12, 2016


#Create class Queue with appropriate methods

class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop(-1)

	def isEmpty(self):
		return self.items == []

#Methods size and peek added for convention, not used in simulation
	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]
#Create a __str__ method to return the queue in string form, and to return "[]" in the case that the queue is empty
	def __str__(self):
		return str(self.items)
		if self.items == []:
			return "[]"

#Initialize the main function
def main():

#Initialize 3 queues for each condition
	Critical = Queue()
	Serious = Queue()
	Fair = Queue()

#Open the text file ERsim.txt, and reach through the "instructions" on each line of the file
	ER = open("ERsim.txt", "r")
	instructions = ER.readlines()
	for line in instructions:

#Split each line to give each instruction as a separate list item
		line = line.strip().split()

#If the first instruction is "exit", end the simulation
		if line[0] == "exit":
			print(">>> Exit")
			return

#If the first instruction is "add", check if the final instruction is Critical, Serious, or Fair, and add the patient to the approriate queue
#After adding a patient, print updated queues
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

#If the first instruction is "treat", check to see if the next instruction is "next", "all", or a specific queue
		if line[0] == "treat":

#If the instructions are to treat "next", treat the next patient, going by rules of queue triage. Print the process
			if line[1] == "next":
				print(">>> Treat next patient")
				print()
				if not Critical.isEmpty():
					print("Treating %s, from Critical queue" % (Critical.dequeue()))
				elif not Serious.isEmpty():
					print("Treating %s, from Serious queue" % (Serious.dequeue()))
				elif not Fair.isEmpty():
					print("Treating %s, from Fair queue" % (Fair.dequeue()))

#If the queues are all empty, move on without printing existing queues
				else:
					print("No patients in queues")
					print()
					continue	

#If a patient was treated, print the updated queues
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

#If the instructions are to treat "Critical", "Serious", or "Fair", print the process of treating the next patient in the corresponding queue (if any exist)
			if line[1] == "Critical":
				print(">>> Treat next patient on Critical Queue")
				print()
				if not Critical.isEmpty():
					print("Treating %s, from Critical queue" % (Critical.dequeue()))
				else:
					print("No patients in queue")
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
					print("No patients in queue")
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
					print("No patients in queue")
					print()
					continue		
				print("Queues are:")
				print("Critical:",Critical)
				print("Serious:",Serious)
				print("Fair:",Fair)
				print()

#If instructed to treat "all", continue treating next until all queues are empty
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
