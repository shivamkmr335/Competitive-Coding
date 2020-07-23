a=int(input())
b=list(map(int,input().split(" ")))
l=list()
for num in range(2,max(b)+ 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           l.append(num)
for j in b:
     for k in l:
          if k*k==j:
               print("YES")
               break
     else:
          print("NO")
