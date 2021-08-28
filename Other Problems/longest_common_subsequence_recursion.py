
def lcs(i,j,a,b):
    if i==len(a) or j==len(b):
        return 0
    if a[i]==b[j]:
        return 1+lcs(i+1,j+1,a,b)
    else:
        return max(lcs(i+1,j,a,b),lcs(i,j+1,a,b))
lcs(0,0,"abedfhr","abcdgh")