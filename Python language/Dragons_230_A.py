s,n=list(map(int,input().split(" ")))
l=list()
for i in range(0,n):
     a,b=list(map(int,input().split(" ")))
     l.append([a,b])
l.sort()
for i in l:
     if s>i[0]:
          s=s+i[1]
     else:
          print("NO")
          break
else:
     print("YES")

          
