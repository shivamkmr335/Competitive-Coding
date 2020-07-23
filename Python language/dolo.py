gh=int(input("enter 1 if booster is on and 0 if not :"))
z=int(input("enter total no of id you would like to know income of together"))
print("enter principal of the ID's:",end=" ",sep="")
acc=[float(i) for i in input().split(' ')]  
te=tuple(acc)
week=int(input("enter the no of weeks for assertion:"))
if gh==1:
    for j in range(0,week):
        for i in range(0,z):
            if acc[i]<=210:
                acc[i]=acc[i]+((acc[i]*5)/100)
            else:
                acc[i]=acc[i]+((acc[i]*4)/100)
print("the principal of the given ID's are : ",end=" ")
for i in acc:
    print(format(i,'.2f'),end='  ')
b=list()
temp=list(te)
sum=0
for i in range(0,z):
    tp=((acc[i]-temp[i])//10)*10
    b.append(tp)
    sum=sum+tp
print("\ndifference is:",b)
print("the total income in dollar is :",sum,"dollars\nThe total income in INR is:",sum*60.375,"rupees")

