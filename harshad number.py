num=int(input())
temp=num
s=0
while num:
    r=num%10
    num=num//10
    s=s+r
if temp%s==0:
    print("true")
else:
    print("false")   
