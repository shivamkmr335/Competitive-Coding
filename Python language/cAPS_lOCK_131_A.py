a=str(input())
s = slice(0,1)
t=slice(1,-1)
if len(a)==1:
    print(a.swapcase())
else:
    u=a[-1]
    b=a[t]
    d=a[s]
    c=b+u
    if c.isupper()==True:
        print(d.swapcase(),c.swapcase(),sep="")

    else:
        print(d,c,sep="")
        


