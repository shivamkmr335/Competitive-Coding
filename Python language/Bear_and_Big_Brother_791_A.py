a,b=list(map(int,input().split(" ")))
count=0
while b>=a:
     a=3*a
     b=b*2
     count=count+1
else:
     print(count)
