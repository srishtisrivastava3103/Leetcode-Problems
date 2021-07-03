#https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
    
def pairsum(a,b,t):
    a1 = 0
    b1 = 0
    v = abs(t-(a[a1]+b[b1]))
    i = 0
    j = len(b)-1
    while i<len(a) and j>=0:
        if v>abs(t-(a[i]+b[j])):
            a1 = i
            b1 = j
            v = abs(t-(a[i]+b[j]))
        if a[i]+b[j]>t:
            j-=1
        else:
            i+=1
                
    return (a[a1],b[b1])
pairsum([1,4,5,7],[10,20,30,40],31)
                
                