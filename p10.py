#12345
#22222
#12345
#44444
#12345
num=int(input())
for i in range(1,num+1):
    if i%2==0:
        for j in range(i,num+i):
            print(i,end=" ")
    else:
        for j in range(1,num+1):
            print(j,end=" ")
    print()
        
