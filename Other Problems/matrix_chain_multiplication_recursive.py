
def mcm(arr,i,j):
    if i>=j:
        return 0
    ans = float('inf')
    for k in range(i,j):
        ans = min(ans,mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j])
    return ans
mcm([40, 20, 30, 10, 30],1,4)
        