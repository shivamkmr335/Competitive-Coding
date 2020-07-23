a=int(input())
b=list(map(int,input().split(" ")))
c=int(input())
d=list(map(int,input().split(" ")))
b.sort()
d.sort()
counter=0
e=len(b)
f=len(d)
for i in range(0,e):
     print(i,"@")
     for j in range(0,f):
          print(j,"%",counter,b,d)
          if abs(b[i]-d[j])<2:
               b.pop(i)
               d.pop(j)
               counter=counter+1
               i=i-1
               j=j-1
               e=e-1
               f=f-1
print(counter)
