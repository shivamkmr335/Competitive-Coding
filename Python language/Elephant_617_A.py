a=int(input())
sum=(a//5)+((a%5)//4)
b=a%5
b=b%4
sum=sum+(b//3)+((b%3)//2)
d=b%3
d=d%2
sum=sum+d
print(sum)

