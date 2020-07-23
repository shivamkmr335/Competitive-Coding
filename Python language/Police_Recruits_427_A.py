a=int(input())
b=list(map(int,input().split(" ")))
count=0
cases=0
for i in b:
    if  i!=(-1):
        count=count+i
    else:
        if count==0:
            cases=cases+1
        else:
            count=count-1
print(cases)
