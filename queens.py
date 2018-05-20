#  File: Queens.py
#  Description: Solve the Queens problem given an input sized square
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: November 10, 2016
#  Date Last Modified: November 10, 2016


#Define class QueensProblem for a grid of a given board size (bSize)
class QueensProblem(object):

#Upon defining a QueensProblem object, create a grid using a 2D list. Use "*" to symbolize an empty space on the board
	def __init__(self, bSize):
		self.b = bSize
		self.board = []
		for i in range(self.b):
			column = []
			for j in range(self.b):
				column.append("*")
			self.board.append(column)
		#define instance variable count to keep track of the number of solutions to the problem
		self.count = 1

#Print the 2D list as a neat grid, representing the current state of the board
	def __str__(self):
		newStr = ""
		counter = 0
		for i in range(self.b):
			for j in range(self.b):
				if counter < self.b - 1:
					newStr += self.board[i][j] + " " 
					counter += 1
				else:
					newStr += self.board[i][j]
					newStr += "\n"
					counter = 0
		return newStr

#Define method isValidPlace to determine if a given spot on a grid is not in the range of any "Q" Queens (diagonally, laterally, etc) 
	def isValidPlace(self,row,col):
		for i in range(self.b):
			for j in range(self.b):
				if i + j == row + col:
					if self.board[i][j] == "Q":
						return False
				if i - j == row - col:
					if self.board[i][j] == "Q":
						return False
				if j == col:
					if self.board[i][j] == "Q":
						return False
				if i == row:
					if self.board[i][j] == "Q":
						return False
		return True

#Define method solve to display and number all possible solutions to the Queens problem of a given board size
	def solve(self, n):

	#if solve recursively gives an n of value 0, it has reached the final row, and may print the solution. return False to continue finding further solutions
		if n == 0:
			print("Solution # %s" % (self.count))
			print(self.__str__())
			self.count += 1
			return False
	#in any given recursion of solve, the row i is determinde by the new number of rows n
		i = n - 1

	#in each recursion, search through every column j of the row
		for j in range(self.b):
			
	#if a space on the grid is valid, place a "Q" for a queen
			if self.isValidPlace(i, j):
				self.board[i][j] = "Q"
	#call on method solve recursively for the next row up
				if self.solve(n - 1):
					return True
				else:
	#when all possibilities have been exhausted for a "Q" in one column, replace it with an empty space and move to the next
					self.board[i][j] = "*"

		return False

#Define the main function
def main():

#Ask the user to input the size of the square board sizeGrid. If the given size is less than 4, keep asking for new inputs
	sizeGrid = eval(input("Enter the size of the square board: "))
	while not sizeGrid >= 4:
		print("Invalid input.")
		sizeGrid = eval(input("Enter the size of the square board: "))
	print()

#Create an object QueensProblem and use method solve to begin printing each solution for the given size
	newBoard = QueensProblem(sizeGrid)
	newBoard.solve(sizeGrid)



main()

