# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

# Time Complexity: O(n2)

def rearrange(arr):
    i = 0
    extras = []
    while i<len(arr):
        if i%2==0 and arr[i]>0:
            k = i+1
            while k<len(arr) and arr[k]>-1:
                k+=1
            if k<len(arr):
                store = arr[k]
                while k>i:
                    arr[k] = arr[k-1]
                    k-=1
                arr[i] = store
            else:
                break
        elif i%2!=0 and arr[i]<0:
            k = i+1
            while k<len(arr) and arr[k]<0:
                k+=1
            if k<len(arr):
                store = arr[k]
                while k>i:
                    arr[k] = arr[k-1]
                    k-=1
                arr[k] = store

            else:
                break
        i+=1
    arr+=extras
    print(arr)
                        
rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])
                






























