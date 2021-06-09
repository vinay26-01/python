def maxsortlen(n,arr):
    if n==0:
        return 0
    count=0
    c=1
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            c+=1
        else:
            count+=1
            c=1
    return (count+1)
                
n=int(input())
data=list(map(int,input().split()))
print(maxsortlen(n,data))
