num=int(input("enter number ="))
c,temp=0,num
rev=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    temp=rev
    c+=1
c=c-2
if temp:
    i=temp%10
    l=temp//10
    j=l%pow(10,c)
    k=rev//pow(10,c+1)
    print(i,end="")
    print(j,end="")
    print(k,end="")
