num=int(input("enter the num: "))
start=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f" {start} ",end=" ")
        start+=1
    print()