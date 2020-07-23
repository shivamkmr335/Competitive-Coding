a=int(input())
b=0
if a%2==0:
     b=a//2
else:
     b=(a//2)+1
s=((a*(a+1))//2)-(2*(b*b))
print(s)
