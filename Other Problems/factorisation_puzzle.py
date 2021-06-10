#Given a number A. B is the product of all factors of A. 
#C is the product of all prime factors of B. D is the number of factors of C.Find D%1000000007.
#Walmart Coding Round

def factorD(A):
    c = 0
    for i in range(2,A//2+1):
        if A%i==0:
            p = 0
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    p+=1
                    continue
            if p==0:
                c+=1
    return c%1000000007

factorD(24)
                
                
                
    
    
    

