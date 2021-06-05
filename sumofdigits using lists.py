def sumofdigits(n,data):
    s=0
    for i in data:
       r=i%10
       i=i//10
       s=s+r
    print(s)
    
n=int(input())
data=list(map(int,input().split()))
t=sumofdigits(n,data)
print(t)
