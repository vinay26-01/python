def search(n,data,s):
    
    c=0
    for i in range(n):
        if data[i]==s:
            c+=1
        if c==2:
            return i
    else:
        return False
n=int(input())
data=list(map(int,input().split()))
s=int(input())
search=search(n,data,s)
print(search)
            
