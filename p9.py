#11111
#12345
#33333
#12345
#55555
num=int(input())
for i in range(1,num+1):
    if i%2==1:
        for j in range(i,num+i):
            print(i,end=" ")
    else:
        for j in range(1,num+1):
            print(j,end=" ")
    print()
        
