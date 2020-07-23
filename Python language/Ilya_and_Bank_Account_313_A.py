a=int(input())
if a>-11 and a<0:
     print(0)
elif a>=0:
     print(a)
elif a<-10:
     a=abs(a)
     b=a%10
     c=(a%100)//10
     if b>=c:
          a=a//10
          print(-a)
     elif b<c:
          a=a//100
          a=(10*a)+b
          print(-a)
