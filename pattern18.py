num=int(input("enter the num "))
for i in range(0,num):
    for j in range(i,-1,-1):
        print(chr(ord('E')-j),end=" ")
    print()