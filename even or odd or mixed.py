num=int(input())
i,j=0,0
while num:
    r=num%10
    num=num//10
    if r%2==0:
        i+=1
    else:
        j+=1
print(i,j)
if i%2==0:
    print("even")
if j%2!=0:
    print("odd")
if i%2!=0 and j%2==0:
    print("mixed")
