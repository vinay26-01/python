n=int(input("enter the number"))
temp=n
i=1
s=0
while n>i:
    if n%i==0: 
        s=s+i 
        i+=1
    if n%i!=0:
        i+=1
           
if s==temp:
         print("perfect number")
else:
         print("not a perfect number")
            

