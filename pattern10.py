num=int(input())
for i in range(1,2*num):
    stars=i
    
    if (num<i):
        stars=2*num-i
    for j in range(0,stars):
        print("*",end=" ")

    print()