"""
1 0 2 0 2 4
"""
def movezeroes(n,arr):
    for i in arr:
        
        if i==0:
            arr.insert(n,0)
            arr.remove(0)
            
n=int(input())
data=list(map(int,input().split()))
movezeroes(n,data)
print(*data)
