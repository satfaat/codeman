# Python program for addition of two matrices
# The order of the matrix is 3 x 3
size1 = 3
size2 = 3

# Function to add matrices mat1[][] & mat2[][],
# and store the result in matrix result[][]
def addMatrices(mat1, mat2, result):
	for i in range(size1):
		for j in range(size2):
			result[i][j] = mat1[i][j] + mat2[i][j]

# driver code
# 1st Matrix
mat1 = [ [9, 8, 7],
	 [6, 8, 0],
	 [5, 9, 2] ]
# 2nd Matrix
mat2 = [ [4, 7, 6],
	 [8, 8, 2],
	 [7, 3, 5] ]
     
# Matrix to store the result
result = mat1[:][:]
# Calling the addMatrices function
addMatrices(mat1, mat2, result)
# Printing the sum of the 2 matrices
print("mat1 + mat2 = ")
for i in range(size1):
	for j in range(size2):
		print(result[i][j], " ", end='')
	print()