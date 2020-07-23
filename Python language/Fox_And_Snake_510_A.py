a,b=list(map(int,input().split()))
count=0
for i in range(0,a):
     if i%2==0:
          for i in range(0,b):
               print("#",end="")
          print("\n",end="")
     elif i%2!=0:
          if count%2==0:
               for i in range(1,b):
                    print(".",end="")
               print("#",end="")
               print("\n",end="")
               count=count+1
          elif count%2!=0:
               print("#",end="")
               for i in range(1,b):
                    print(".",end="")
               print("\n",end="")
               count=count+1
