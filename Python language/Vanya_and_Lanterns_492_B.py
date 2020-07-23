a,b=list(map(int,input().split(" ")))
c=list(map(int,input().split(" ")))
c.sort()
d=list()
e=abs(0-c[0])
f=abs(b-c[-1])
for i in range(0,a-1):
     d.append(abs(c[i]-c[i+1]))
if len(d)==0 or a==1:
     g=max(e,f)
     print("%0.10f"%(g))
else:
     g=(max(d))/2
     if g>e and g>f:
          print("%0.10f"%(g))
     else:
          print("%0.10f"%(max(e,f)))

