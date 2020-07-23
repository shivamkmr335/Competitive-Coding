a=list()
for i in range(3,361):
     b=180-(360/i)
     a.append(b)
c=int(input())
for j in range(0,c):
     d=float(input())
     if d in a:
          print("YES")
     else:
          print("NO")

          
