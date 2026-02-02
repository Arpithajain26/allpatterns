num=int(input("enter the number"))
for i in range(1,num+1):
    for j in range(i):
        print(chr(ord('A')+j),end=" ")
    print()