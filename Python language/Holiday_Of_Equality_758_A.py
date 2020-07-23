a=int(input())
b=list(map(int,input().split(" ")))
c=max(b)
s=0
for i in b:
     s=s+(c-i)
print(s)
     
