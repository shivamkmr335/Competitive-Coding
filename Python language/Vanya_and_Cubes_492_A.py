a=int(input())
b=0
c=0
d=0
for i in range(1,a+1):
     b=b+i
     d=d+b
     if d<=a:
          c=c+1
     else:
          break
print(c)
