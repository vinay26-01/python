def issorted(n,data):
    aes=0
    des=0
    for i in range(n-1):
        if data[i]>data[i+1]:
            des+=1
        if data[i]<data[i+1]:
            aes+=1

        if aes!=0 and des!=0:
            return False
    return True
n=int(input())
data=list(map(int,input().split()))
print(issorted(n,data))
