num=int(input()) #234567
s=0
j=0
while num: #234567 
    r=num%10 #7 ,#6 , #5 #4
    num=num//10 #23456 , #2345 ,#234 ,#23
    s=s+r #7 , #13 ,#18, #22
if num==0:
    print(s)
    if s>9:
        k=s%10 #7 
        j=s//10 #2
        j=j+k
        print(j)
        



 
