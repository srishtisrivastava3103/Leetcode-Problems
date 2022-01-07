# Given an array of N numbers, we need to maximize the sum of selected numbers. 
# At each step, you need to select a number Ai, delete one occurrence of it and delete all occurrences of 
# Ai-1 and Ai+1 (if they exist) in the array.
# Repeat these steps until the array gets empty. The problem is to maximize the sum of the selected numbers.
# For Example:
# [1, 2, 2, 2, 3, 4] -> 10, delete 2,4
# [1,2,2,3,3,3,3,4] -> 13, delete 1 and 3

def maximize_sum(array):
    freq = [0]*(max(array)+1)
    for num in array:
        freq[num]+=1
    maxSum = [freq[0]*0, freq[1]*1]
    for idx in range(2,len(freq)):
        maxSum.append(max(maxSum[idx-2]+freq[idx]*idx,maxSum[idx-1]))
    return maxSum[-1]
maximize_sum([1,2,2,2,2,2,2,2,2,2,3,4])
        
        