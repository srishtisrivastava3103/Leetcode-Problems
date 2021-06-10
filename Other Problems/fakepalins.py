#All possible fake palindrome substrings (Fake palindrome- whether a string has any possibilities of palindrome)
# Input: ABAB => A, B, A ,B, ABA ,BAB ,ABAB 
#        (ABAB can make it to BAAB or ABBA )
# Output:  7

def fakepalins(s):
    c = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            t = s[i:j+1]
            if t==t[::-1]:
                c+=1
                print(t)
            else:
                f = 0
                for k in range(len(t)):
                    if t.count(t[k])%2!=0:
                        f+=1
                if f<=1:
                    c+=1
                    print(t)
    return c
                                            
                    
fakepalins("ABBA")