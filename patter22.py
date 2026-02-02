num=int(input("enter the number: "))
for i in range(0,num):
    for j in range(0,num):
        if (i==0 or j==0 or i==(num-1) or j==(num-1)):
            print(7,end=" ")
        elif (i==1 or j==1 or j==(num-2) or i==(num-2)):
            print(3,end=" ")
        elif (i==2 or j==2 or j==(num-3) or i==(num-3)):
            print(2,end=" ")
        else:
            print(1,end=" ")
    print()