a,b=list(map(int,input().split(" ")))
c=list(map(int,input().split(" ")))
c.sort()
diff=c[-1]-c[0]
for i in range(0,b-a+1):
     if (c[i+a-1]-c[i])<diff:
          diff=c[i+a-1]-c[i]
print(diff)

