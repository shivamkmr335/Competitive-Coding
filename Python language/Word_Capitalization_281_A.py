a=list(input())
b=a[0].upper()
print(b,end="")
a.pop(0)
for i in a:
    print(i,sep="",end="")
