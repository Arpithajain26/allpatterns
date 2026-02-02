num=int(input("enter the number"))
for i in range(0,num):
    # space
    for j in range(0,num-i-1):
        print(" ",end=" ")
    # char
    for j in range(i+1):
        print(chr(ord('A')+j),end= " ")
    for j in range(i-1,-1,-1):
        print(chr(ord('A')+j),end=" ")
    for j in range(0,num-i-1):
        print(" ",end=" ")
    print()
    