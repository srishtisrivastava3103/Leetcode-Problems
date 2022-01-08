# Maximize a-b+c-d in an array where a<b<c<d

def maximizeExpression(array):
    # Write your code here.
    if len(array)<4:
		return 0
	first = [float('-inf')]
	a = float('-inf')
	b = float('inf')
	for i in range(1,len(array)-2):
		if array[i-1]>a:
			a = array[i-1]
		if array[i]<b:
			b = array[i]
		first.append(max(first[i-1],a-b))
	second = [float('-inf'),float('-inf')]
	a_b = first[1]
	c = array[2]
	for i in range(2,len(array)-1):
		a_b = first[i-1]
		c = array[i]
		second.append(max(second[i-1],a_b+c))
	third = [float('-inf')]*3
	d = array[3]
	a_b_c = second[2]
	for i in range(3,len(array)):
		# if second[i-1]<a_b_c:
		a_b_c = second[i-1]
	# if array[i]<d:
		d = array[i]
		third.append(max(third[i-1],a_b_c-d))
	print(first,second,third)
	return third[-1]
