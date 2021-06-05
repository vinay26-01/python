def min_max(n,data):
    small=data[0]
    large=data[0]

    for i in data:
        if small>i:
            small=i
        if large<i:
            large=i
    return small,large
        
n=int(input())
data=list(map(int,input().split()))
min,max=min_max(n,data)
print(min,max)
