num=int(input("enter number = "))
temp=num
maximum=0
minimum=9
while num:
    r=num%10
    num=num//10
    if r>maximum:
         maximum=r
print("maximum = ",maximum)
while temp: 
    i=temp%10 
    temp=temp//10
    if i<minimum:
     minimum=i
print("minimum =",minimum)
