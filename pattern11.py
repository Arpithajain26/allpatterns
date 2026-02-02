num=int(input("enter the number"))
start=1
for i in range(0,num):
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(0,i+1):
        print(f"{start}",end="")
        start=1-start
    print()
    