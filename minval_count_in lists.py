def find_min(n,data):
    s=data[0]
    c=0
    for i in data:
        if s==i:
            c+=1
        if s>i:
            s=i
            c=1
    ind=[s,c]
    for i in range(n):
        if s==data[i]:
            ind.append(i)
    return ind
        
n=int(input())
data=list(map(int,input().split()))
minval=find_min(n,data)
print(*minval)
