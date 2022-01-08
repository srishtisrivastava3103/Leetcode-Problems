# https://www.geeksforgeeks.org/maximum-sum-submatrix/


def maximumSumSubmatrix(matrix, size):
    # Write your code here.
	if len(matrix)==0 or len(matrix)<size or len(matrix[0])<size:
		return matrix
	sums = [[matrix[0][0]]]
	for i in range(1,len(matrix[0])):
		sums[0].append(sums[0][-1]+matrix[0][i])
	print(sums)
	for i in range(1,len(matrix)):
		sums.append([])
		for j in range(len(matrix[0])):
			if j==0:
				sums[-1].append(sums[i-1][0]+matrix[i][j])
			else:
				sums[-1].append(sums[i-1][j]+sums[i][j-1]-sums[i-1][j-1]+matrix[i][j])
	print(sums)
	maxSum = float('-inf')
	maxSumSubmatrix = [0,0]
	for row in range(size-1,len(matrix)):
		for col in range(size-1,len(matrix[0])):
			if row-size>=0 and col-size>=0:
				sum = sums[row][col]-sums[row-size][col]-sums[row][col-size]+sums[row-size][col-size]
			elif row-size>=0:
				sum = sums[row][col]-sums[row-size][col]
			elif col-size>=0:
				sum = sums[row][col]-sums[row][col-size]
			else:
				sum = sums[row][col]
			print(sum)
			if sum>maxSum:
				# print(maxSum)
				maxSum = sum
				maxSumSubmatrix = [row,col]
	subMatrix = []
	print(maxSum)
	for row in range(maxSumSubmatrix[0]-size+1,maxSumSubmatrix[0]+1):
		subMatrix.append([])
		for col in range(maxSumSubmatrix[1]-size+1,maxSumSubmatrix[1]+1):
				subMatrix[-1].append(matrix[row][col])
	# return subMatrix
	print(subMatrix)
	return maxSum
			
			
			

