a=int(input())
b=list(map(int,input().split(" ")))
c=list()
for i in range(0,a):
     d=list()
     for j in range(0,b[i]):
          d.append(1)
     c.append(d)
c.sort()
for i in range(0,a):
     e=c[i].count(1)
     print(e,end=" ")
          
