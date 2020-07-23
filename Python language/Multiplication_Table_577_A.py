a,b=list(map(int,input().split(" ")))
count=0
for i in range(1,a+1):
     for j in range(1,a+1):
          if i<=b and j<=b:
               if (i*j)==b:
                    count=count+1
          else:
               break
print(count)
