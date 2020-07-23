i=int(input())
l=list()
count=0
for i in range(0,i):
    a=str(input())
    b=a.find("++")
    c=a.find("--")
    if b!=-1:
        count=count+1
    if c!=-1:
        count=count-1
print(count)
