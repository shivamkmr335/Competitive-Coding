a=int(input())
b=list(map(int,input().split(" ")))
c=b.count(1)
d=b.count(2)
e=b.count(3)
one=0
three=0
#set of 4 is taken out
total=b.count(4)
#pair of 2 is created and taken out
total=total+d//2
#tl stands for 2 left
#here 2 is first combined with one
tl=d%2
#if 2 are left after pairing of two
if tl != 0:
    if c>2:
        c=c-2
    else:
        c=0
    total=total+1
    if c>=e:
        c=c-e
    else:
        c=0
    total=total+e    
#now if 2 was left,it is removed by pairing with one
else:
    if c>=e:
        c=c-e
    else:
        c=0
    total=total+e
if c%4==0:
    total=total+(c//4)
else:
    total=total+(c//4)+1
print(total)
    
