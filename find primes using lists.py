import math as m
def isprime(num):
        if num==1:
            
            return 0
        s=int(m.sqrt(num))
        for i in range(2,s+1):
            if num%i==0:
                return 0
        return 1
        
    
def findprimes(n,data):
    prime=[]
    
    for i in data:
        if isprime(i):
            
            prime.append(i)
    return prime
n=int(input())
data=list(map(int,input().split()))
primes=findprimes(n,data)
print(*primes)
