a,b=list(map(int,input().split(" ")))
d=1*(10**a)
c=1*(10**(a-1))
for i in range(c,d):
     f=i
     s=0
     while f>0:
          s=s+(f%10)
          f=f//10
     if s==b:
          print(i,end=" ")
          break
else:
     print(-1,end=" ")
for j in range(d-1,c-1,-1):
     f=j
     s=0
     while f>0:
          s=s+(f%10)
          f=f//10
     if s==b:
          print(j)
          break
else:
     print(-1)
     
