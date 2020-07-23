a,b=list(map(int,input().split(" ")))
c=a
d=0
while a>0 or d>b:
    c=c+(a//b)
    d=d+(a%b)
    if (d//b)>0:
        c=c+d//b
        d=d%b
    a=a//b
print(c)
