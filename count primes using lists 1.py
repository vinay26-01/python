import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
        
    
def countprimes(n,data):
    res=0
    for i in data:
        if isprime(i):
            res+=1
    return res
        
n=int(input())
data=list(map(int,input().split()))
pc=countprimes(n,data)
print(pc)
