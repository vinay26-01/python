def total_marks(n,data):
    k=0
    for i in range(n):
        k=k+data[i]
    return k
        
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)
