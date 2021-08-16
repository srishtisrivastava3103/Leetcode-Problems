# Print all permutations of a given string

ans = []
def allperm(s,l,r):
    if l==r:
        print(''.join(s))
        ans.append(''.join(s))
        return
    for i in range(l,r+1):
        s[i],s[l] = s[l],s[i]
        allperm(s,l+1,r)
        s[i],s[l] = s[l], s[i]

allperm(['a','b','c'],0,2)
    