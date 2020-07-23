a=int(input())
b=list()
count=1
for i in range(0,a):
    c=int(input())
    b.append(c)
for i in range(1,a):
    if b[i]!=b[i-1]:
        count=count+1
print(count)
