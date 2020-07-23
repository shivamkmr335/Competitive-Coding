l=list()
for i in range(1,6):
    temp=list(map(int,input().split(" ")))
    l=l+temp
a=l.index(1)+1
if a%5==0:

    row=a//5
else:
    row=(a//5)+1
column=(a%5)
if column==0:
    column=5
diff=abs(3-row)+abs(3-column)
print(diff)


