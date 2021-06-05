def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def find_min(n,data):
    for i in data:
        i=min(data)
        s=reverse(i)
    return i,s
n=int(input())
data=list(map(int,input().split()))
minval=find_min(n,data)
print(*minval)
