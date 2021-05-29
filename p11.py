#10101
#01010
#10101
#01010
#10101
num=int(input())
for i in range(1,num+1):
    if i%2==1:
        for j in range(1,num+1):
            if j%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    else:
        for j in range(1,num+1):
            if j%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
    print()
