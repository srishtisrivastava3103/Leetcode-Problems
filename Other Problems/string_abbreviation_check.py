#Check whether two strings are equivalent or not, one of them being an abbreviation of the other. (Case-Insensitive)
#For example String: Internationalization Abbr: I18n where 18 are the number of characters between I and N
#String: Poster Abbr: P1s2r  

def character_abbrev(st,ab):
    i = 0
    j = 0
    while i<len(st) and j<len(ab):
        if ab[j].isalpha():
            if ab[j]!=st[i]:
                return False
            else:
                i+=1
                j+=1
        else:
            num = ab[j]
            j+=1
            while(j<len(ab) and ab[j].isnumeric()):
                num = num+ab[j]
                j+=1
            num = int(num)
            if st[i+num]!=ab[j]:
                return False
            else:
                i+=num+1
                j+=1
    if i==len(st) and j==len(ab):
        return True
    
    return False
character_abbrev("Poster", "P1s2r")        
        