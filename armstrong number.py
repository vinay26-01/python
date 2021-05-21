def armstrong(n):
    temp=n
    dc=0
    while temp:
        temp=temp//10
        dc+=1
    s=0
    temp=n
    while temp: #153 #15 #1
        r=temp%10 #3 #5 #1
        temp=temp//10 #15 #0
        s+=pow(r,dc) #9 #9+125 #9+125+27
    if n==s:
        return True
    return False
n=int(input())
print(armstrong(n))
