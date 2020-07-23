n=int(input())
a=[]
sum=0
temp=0
a=list(map(int,input().split(" ")))
a.sort(reverse=True)
for i in range(0,n):
    sum=sum+a[i]
for j in range(0,n):
    temp=temp+a[j]
    diff=sum-temp
    if temp > diff:
        print(j+1)
        break
    elif temp==diff:
        print(j+2)
        break
