a=int(input())
b=str(input())
c=b.lower()
d=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in d:
     if i in c:
          s=0
     else:
          print("NO")
          break
else:
     print("YES")
