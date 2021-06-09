"""
1 1 1 1 2 1 1 1 2 1 1 1
"""
def maximum1s(n,data):
    c=0
    d=[]
    for i in range(n):
        
        if data[i]==1:
            c+=1
        else:
                
            d.append(c)
            c=1
            
    return(max(d))
n=int(input())
data=list(map(int,input().split()))
print(maximum1s(n,data))
