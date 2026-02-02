def pattern7(num):
    for i in range(0,num):
        for j in range(0,num-i-1):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,num-i-1):
            print(" ",end="")
        print()
def pattern8(num):
    for i in range(0,num):
        for j in range(0,i):
            print(" ",end="")
        for j in range(2*num-(2*i+1),0,-1):
            print("*",end="")
        for j in range(0,i):
            print(" ",end="")
        print()
pattern7(4)
pattern8(4)
