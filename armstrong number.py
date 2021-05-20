n=int(input("enter the number"))
temp=n
i=0
while n!=0: #153 #15 #1
    r=n%10 #3 #5 #1
    n=n//10 #15 #0
    i=i+pow(r,3) #9 #9+125 #9+125+27
if temp==i:
        print("armstrong number")
else:
        print("not a armstrong number")
