num=int(input("enter the number"))
for i in range(num,0,-1):
    for j in range(i):
        print(chr(ord('A')+j),end=" ")
    print()