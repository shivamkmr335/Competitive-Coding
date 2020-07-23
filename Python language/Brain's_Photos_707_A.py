a,b=list(map(int,input().split(" ")))
c=list()
for i in range(0,a):
     d=list(map(str,input().split(" ")))
     c.append(d)
     
for i in c:
     if 'C' in i or 'M' in i or 'Y' in i:
          print("#Color")
          break
else:
     print("#Black&White")
