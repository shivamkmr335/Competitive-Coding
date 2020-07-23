size=int(input())
a=list(input())
print(a,size,"/*-+*/")
for i in range(0,size-1):
    if (a[i]=='1' and a[i+1]=='0') or  (a[i]=='0' and a[i+1]=='1'):
        a.pop(i)
        a.pop(i)
        i=i-1
        size=size-2
        print(a,size)
    else:
        print("blank",size)
    print('***',i,"***")
        
        
