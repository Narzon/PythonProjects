#  File: Grid.py

#  Description: Given a square grid of positive integers with dimensions that are divisible by 4, find the greatest product of 4 integers that are adjacent horizontally, vertically, or diagonally.

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 14, 2016

#  Date Last Modified: April 14, 2016

def main():

#open the grid in "grid.txt", and read the dimensions in the first line as an integer. assign this to variable dim
   in_file = open("grid.txt", "r")
  
   dim = in_file.readline()
   dim = int(dim.strip())

#intialize the variable max_prod for the highest product in the grid
   max_prod = 0

#initialize grid as a 2D list of integers using each line of the file
   grid = []
   for i in range (dim):
      rows = in_file.readline().strip( )
      rows = rows.split()
      for j in range (dim):
         rows[j] = int(rows[j])
      grid.append(rows)
   in_file.close()

#read the numbers horizontally, row by row. if the product of any 4 adjacent are higher than max_prod, replace it
   for row in grid:
      for i in range (0, len(row) - 3):
         num_row = 1
         for j in range (i, i + 4):
            num_row = num_row * row[j]
            if num_row > max_prod:
               max_prod = num_row

#read the numbers vertically, column by column. if the product of any 4 adjacent are higher max_prod, replace it
   for j in range (dim):
      for i in range (0, dim - 3):
         num_col = 1
         for k in range (i, i + 4):
            num_col = num_col * grid[k][j]
            if num_col > max_prod:
               max_prod = num_col

#read the numbers diagonally, going downwards left-to-right. if the product of any 4 adjacent are higher than max_prod, replace it
   for j in range (0, dim - 3):
      for i in range (0, dim - 3):
         num_diagdown = 1
         for h in range (0, 4):
            num_diagdown = num_diagdown * (grid[i + h][j + h])
            if num_diagdown > max_prod:
               max_prod = num_diagdown

#read the numbers diagonally, going upwards left-to-right. if the product of any 4 adjacent are higher than max_prod, replace it
   for j in range (0, dim - 3):
      for i in range (3, dim):
         num_diagup = 1
         for g in range (0, 4):
            num_diagup = num_diagup * (grid[i - g][j + g])
            if num_diagup > max_prod:
               max_prod = num_diagup

#print the maximum product found
   print("The greatest product is %s." % max_prod)










main()