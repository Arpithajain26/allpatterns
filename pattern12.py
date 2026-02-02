num=int(input("enter the number"))
for i in range(0,num+1):
    for j in range(1,i+1):
        print(f"{j}",end="")
    for j in range(2*num-(2*i),0,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(f"{j}",end="")
    print()
    