# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

def palinpartition(s,i,j):
    print("count")
    if i>=j:
        return 0
    if s[i:j+1]==s[i:j+1][::-1]:
        return 0
    ans = float('inf')
    for k in range(i,j):
        temp = palinpartition(s,i,k)+palinpartition(s,k+1,j)+1
        ans = min(ans,temp)
    return ans
palinpartition("aaaa",0,3)