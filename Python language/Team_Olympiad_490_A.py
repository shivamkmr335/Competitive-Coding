a=int(input())
b=list(map(int,input().split(" ")))
one=b.count(1)
two=b.count(2)
three=b.count(3)
print(min(one,two,three))
while b.count(1)!=0 and b.count(2)!=0 and b.count(3)!=0:
     c=b.index(1)
     d=b.index(2)
     e=b.index(3)
     b.remove(1)
     b.insert(c,0)
     b.remove(2)
     b.insert(d,0)
     b.remove(3)
     b.insert(e,0)
     print(c+1,d+1,e+1)
     
