a=int(input())
name={}
for i in range(0,a):
    b=input()
    if b not in name:
        name[b]=0
        print("OK")
    else:
        name[b]+=1
        print(b+str(name[b]))
