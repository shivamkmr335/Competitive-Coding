a=int(input())
while a!=-1:
     a=a+1
     if a//1000!=(a%1000)//100 and (a%1000)//100!=(a%100)//10 and (a%100)//10!=a%10 and a//1000!=(a%100)//10 and a//1000!=a%10 and (a%1000)//100!=a%10:
          print(a)
          break


          
