a=int(input())
b=list()
count=0
for i in range(0,a):
    c=list(map(int,input().split(" ")))
    b.append(c)
    if (b[i][1]-b[i][0]) >=2:
        count=count+1
print(count)
