input()
a=list(map(int,input().split()))
d=[0]*(max(a)+1)
for x in a:
    d[x]+=x
print(d)
