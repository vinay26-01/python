def count(n,data):
    ec=0
    oc=0
    for i in range(n):
        if data[i]%2==0:
            ec+=1
        else:
            oc+=1
    return ec,oc
            
        
n=int(input())
data=list(map(int,input().split()))
count=count(n,data)
print(*count)
