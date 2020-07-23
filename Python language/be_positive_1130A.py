a=int(input())
b=list(map(int,input().split()))
b.sort()
print(b)
j=0
count=0
while(b[j]<0):
    j+=1
pos=a-j
if pos > j:
    print(1)
elif j>pos:
    print(-1)
else:
    print(0)
