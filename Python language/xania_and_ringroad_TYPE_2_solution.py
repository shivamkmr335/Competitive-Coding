a,b=list(map(int,input().split(" ")))
c=list(map(int,input().split(" ")))
c.sort()
l=list()
for i in c:
     d=c.count(i)
     l.append([i,d])
     for j in range(0,d):
          c.remove(i)
n=list()
m=list()
for j in l:
     n.append(j[0])
     m.append(j[1])
mx=max(m)
ind=m.index(mx)
sub=n[ind]
print(l,m,n,mx,ind,sub)
print((a*(mx-1))+(sub-1))
