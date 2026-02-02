num=int(input("enter the number"))
for i in range(0,num):
    for j in range(i+1):
        print(chr(ord('A')+i),end=" ")
    print()