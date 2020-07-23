a=int(input())
b=list(map(int,input().split(" ")))
c=b.index(0)+1
print(b)
b.reverse()
l=len(b)
d=l-(b.index(0))
print(a,b,c,d,l)
one=b.count(1)
zero=b.count(0)
out_1=(c-1)+(l-d)
in_1=one-out_1
print(out_1,in_1)
