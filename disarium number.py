num=int(input())
temp=k=num
s=0
t=0
while num:
    r=num%10
    num=num//10
    s+=1
while temp:
    r=temp%10
    temp=temp//10
    t=t+pow(r,s)
    s-=1
if k==t:
    print("true")
else:
    print("false")
