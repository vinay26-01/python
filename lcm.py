a,b=map(int,input().split())
t=2
s=1
while t<=a and t<=b: #2 6 #1 3
      if a%t==0 and b%t==0:
          a=a//t #1
          b=b//t #3
          s=s*t
      else:
          t+=1
s=s*a*b
print(s)
