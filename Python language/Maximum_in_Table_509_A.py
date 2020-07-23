a=int(input())
b=list()
c=list()
for i in range(0,a):
    c.append(1)
b.append(c)
for i in range(1,a):
    d=[1]
    b.append(d)
for j in range(1,a):
    for k in range(1,a):
        e=b[j-1][k]+b[j][k-1]
        b[j].append(e)
print(b[a-1][a-1])

    
