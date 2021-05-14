num=int(input("enter number = ")) 
max,min=num%10,num%10 
maximumcount=0
minimumcount=0
while num: 
    r=num%10 
    num=num//10 
    if max<r: 
        max=r 
        maximumcount=1 
    elif max==r: #1==r=1 
         maximumcount+=1 
    if min>r:#1>2 (false)
        minimumcount=1
        min=r
    elif min==r:
        minimumcount+=1
print("maximum =",max,"maximun count =",maximumcount)
print("minimum = ",min,"minimum count =",minimumcount)
        
