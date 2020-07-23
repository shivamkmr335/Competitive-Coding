a=int(input())
l=list()
for num in range(2,a + 1):
     for i in range(2,num):
          if (num % i) == 0:
               l.append(num)
               break
b=len(l)
for i in range(0,b):
     for j in range(b-1,0,-1):
          if (l[i]+l[j])==a:
               print(l[i],l[j])
               break
     if (l[i]+l[j])==a:
          break

