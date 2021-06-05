def old_data(n,data):
    d=[]
    for i in data:
        if i not in d:
            d.append(i)
    return d
n=int(input())
data=list(map(int,input().split()))
new=old_data(n,data)
print(*new)
