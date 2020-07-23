import math
a,b,n=list(map(int,input().split(" ")))
count=0
while n>0:
    if count%2==0:
        c=math.gcd(a,n)
    else:
        c=math.gcd(b,n)
    n=n-c
    count=count+1
else:
    if count%2==0:
        print(1)
    else:
        print(0)
        
