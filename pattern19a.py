num=int(input("enter the num: "))
for i in range(0,num):
    # stars
    for j in range(num-i,0,-1):
        print("*",end=" ")
    for j in range(2*i):
        print(" ",end=" ")
    for j in range(num-i,0,-1):
        print("*",end=" ")
    print()
for i in range(0,num):
    for j in range(i+1):
        print("*",end=" ")
    for j in range((2*num)-(2*i)-2):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print("*",end=" ")
    print()