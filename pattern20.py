num=int(input())
for i in range(1,2*num):
    stars=i
    
    if (num<i):
        stars=2*num-i
    for j in range(0,stars):
        print("*",end=" ")
    stars=(2*num)-(2*i)
    k=1
    if (num<i):
        stars=i-(2*num-i)
    for j in range(stars):
        print(" ",end=" ")
    # another
    stars=i
    
    if (num<i):
        stars=2*num-i
    for j in range(stars,0,-1):
        print("*",end=" ")
    
    

    
    

    print()