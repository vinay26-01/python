n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

        
