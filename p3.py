#6
#1 2 3 4 5 6 
#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1
num=int(input())
for i in range(0,num):
    for j in range(1,num-i+1):
        print(j,end=" ")
    print()
