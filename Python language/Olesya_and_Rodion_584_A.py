a,b=list(map(int,input().split(" ")))
c=10**(a-1)
while c<(10**a):
     if c%b==0:
          print(c)
          break
     c=c+1
else:
     print(-1)
     
