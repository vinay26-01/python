def rev(num):
    rev1=0
    while num:
        r=num%10
        num=num//10
        rev1=rev1*10+r
    return rev1

def reverse(n,data):
    for i in range(n):
        data[i]=rev(data[i])
    return data[i]
        

n=int(input())
data=list(map(int,input().split()))
reverse(n,data)
print(*data)
