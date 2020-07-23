a=int(input())
b=str(input())
c=b.count('A')
d=b.count('D')
if c>d:
    print("Anton")
elif c==d:
    print("Friendship")    
else:
    print("Danik")
