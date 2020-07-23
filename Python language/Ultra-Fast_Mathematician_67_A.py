a=list(input())
b=list(input())
c=list()
for i in range(0,len(a)):
     if a[i]==b[i]:
          c.append(0)
     else:
          c.append(1)
     print(c[i],end="")
