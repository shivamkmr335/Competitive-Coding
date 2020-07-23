a=list(map(int,input().split(" ")))
b=a.count(a[0])
c=a.count(a[1])
d=a.count(a[2])
e=a.count(a[3])
if b==1 and c==1 and d==1 and e==1:
     print(0)
elif b==2 and ((c==1 and d==1 and e==2) or (c==2 and d==1 and e==1) or (c==1 and d==2 and e==1)):
     print(1)
elif c==2 and ((b==1 and d==1 and e==2) or (b==2 and d==1 and e==1) or (b==1 and d==2 and e==1)):
     print(1)
elif d==2 and ((c==1 and b==1 and e==2) or (c==2 and b==1 and e==1) or (c==1 and b==2 and e==1)):
     print(1)
elif e==2 and ((c==1 and d==1 and b==2) or (c==2 and d==1 and b==1) or (c==1 and d==2 and b==1)):
     print(1)
elif b==2 and c==2 and d==2 and e==2:
     print(2)
elif b==3 or c==3 or d==3 or e==1:
     print(2)
elif b==4:
     print(3)
