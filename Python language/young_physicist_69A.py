a=int(input())
b=list()
x=0
y=0
z=0
for i in range(0,a):
    c=list(map(int,input().split(" ")))
    b.append(c)
    x=x+b[i][0]
    y=y+b[i][1]
    z=z+b[i][2]
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")
    
    
