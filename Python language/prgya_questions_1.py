a=int(input())
b=a
temp=1
tem=1
for i in range(0,a):
     for j in range(0,2*i):
          print("*",sep="",end="")
     for k in range(i,a):
          print(temp,0,sep="",end="")
          temp=temp+1
     for k in range(i,a):
          print((b*b)+tem,sep="",end="")
          while k<(a-1):
               print(0,end="")
               break
          
          tem=tem+1
     b=b-1
     print(" ")
     

