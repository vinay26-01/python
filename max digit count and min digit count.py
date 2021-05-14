num=int(input("enter number = ")) #1231
max,min=num%10,num%10 #1,1
maximumcount=0
minimumcount=0
while num: #1231 #123 #12
    r=num%10 #1 #3 #2
    num=num//10 #123 #12 #1
    if max<r: #1<1 (false) #3<12 #3<2(false)
        max=r #3
        maximumcount=1 #1
    elif max==r: #1==r=1 #3==2(false)
         maximumcount+=1 #2
    if min>r:#1>2 (false)
        minimumcount=1
        min=r
    elif min==r:
        minimumcount+=1
print("maximum =",max,"maximun count =",maximumcount)
print("minimum = ",min,"minimum count =",minimumcount)
        
