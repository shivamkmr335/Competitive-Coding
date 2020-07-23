a=int(input(""))
b=int(input(""))
for l in range(0,a):
    print(" ",end="")
print("*")
for i in range(1,a):
    for j in range(1,a-i):
        print(" ",end="")
    if (1+i)==b:
        for g in range(0,(2*b)+1):
            print("*",end="")
        print("")
    else:
        print("*",end="")
        for k in range (0,1+(2*i)):
            print(" ",end="")
        print("*")
        
