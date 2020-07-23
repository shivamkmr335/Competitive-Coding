a=int(input())
b=list(map(int,input().split(" ")))
c=b[0]
max=c
min=c
count=0
for i in range(1,a):
    if b[i]>max:
        max=b[i]
        count=count+1
    elif b[i]<min:
        min=b[i]
        count=count+1
print(count)
