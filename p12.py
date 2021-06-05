#     *
#    *  *
#   ******
#  *      *
# *        *
num=int(input())
a=int(input())
for i in range(1,num+1):
    for j in range(1,num+1):
        if j<num:
            print("",end=" ")
        if j==num:
            print("*",end=" ")
    num-=1
    
    for j in range(num+1,a+1):
                if j==a:
                     print("*",end=" ")

                if j<a:
                    print("",end=" ")
    a+=1
    
    
                    
                    
            

    print()
