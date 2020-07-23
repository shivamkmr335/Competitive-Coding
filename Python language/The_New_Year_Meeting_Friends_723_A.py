a=list(map(int,input().split(" ")))
a.sort()
c=a[1]
print(abs(a[0]-c)+abs(a[2]-c))
