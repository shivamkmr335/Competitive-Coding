a=input()
b=str(input())
c=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","/"]
temp=0
if a=='L':
     temp=temp+1
else:
     temp=temp-1
for i in b:
     d=c.index(i)
     print(c[d+temp],end="")

