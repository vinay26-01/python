n=int(input())
temp=0
i=0
k=0
while n: #19
    r=n%10 #9 #1
    n=n//10 #0
    i=i+pow(r,2) #8
    if n==0 and i>=10:
        n=i
    print(n)
    i=0
if i<10:
     Print(i)
    
