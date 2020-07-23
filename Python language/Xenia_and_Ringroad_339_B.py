a,b=list(map(int,input().split(" ")))
c=list(map(int,input().split(" ")))
count=0
p=1
for i in c:
     if i==p:
          count=count+0
     elif i>p:
          count=count+(i-p)
          p=i
     elif i<p:
          count=count+(a-p)+i
          p=i
print(count)
          
     
