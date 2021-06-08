def secondlargest(n,data):
    data=list(set(data))
    data.sort()
    return data[-2]
n=int(input())
data=list(map(int,input().split()))
print(secondlargest(n,data))
