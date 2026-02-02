def pattern19(num):
    for i in range(num):
        # left stars
        for j in range(num - i):
            print("*", end=" ")

        # middle spaces (FIXED)
        for j in range(2* i):
            print(" ", end=" ")

        # right stars
        for j in range(num - i):
            print("*", end=" ")

        print()
def pattern19a(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        for j in range(2*num-(2*i),0,-1):
            print(" ",end=" ")
        for j in range(i,0,-1):
            print("*",end=" ")
        print()
pattern19(5)
pattern19a(5)
        
    