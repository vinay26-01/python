num=int(input())
for i in range(1,num+1):
    if i%2==0:
        for j in range(num-i+1,0,-1):
            print(j,end="")
    else:
        for j in range(1,num-i+2):
            print(j,end="")
    print()
            
