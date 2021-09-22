# https://www.geeksforgeeks.org/smallest-difference-pair-values-two-unsorted-arrays/

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    smallest = float('inf')
    smallest_i = arrayOne[i]
    smallest_j = arrayTwo[i]
    while i<len(arrayOne) and j<len(arrayTwo):
        curr_i = arrayOne[i]
        curr_j = arrayTwo[j]
        if arrayOne[i]<arrayTwo[j]:
            current = arrayTwo[j]-arrayOne[i]
            i+=1
        elif arrayOne[i]>arrayTwo[j]:
            current  = arrayOne[i]-arrayTwo[j]
            j+=1
        else:
            return [arrayOne[i],arrayTwo[j]]
        if smallest>current:
            smallest = current
            smallest_i = curr_i
            smallest_j = curr_j
    return [smallest_i,smallest_j]