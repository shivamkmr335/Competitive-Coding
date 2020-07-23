a,e=list(map(int,input().split(' ')))
if a%2==0:
    if e<=(a//2):
        print((2*e)-1)
    else:
        e=e-(a//2)
        print(2*e)
else:
    if e<=((a//2)+1):
        print((2*e)-1)
    else:
        e=e-((a//2)+1)
        print(2*e)
    
