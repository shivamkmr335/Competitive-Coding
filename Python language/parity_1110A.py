b,k=list(map(int,input().split(' ')))
a=list(map(int,input().split()))
temp=0
for i in range(0,k):
    n=0
    n=(a[i]*(b**(k-i-1)))
    if n%2!=0:
        temp+=1
if temp%2==0:
    print("even")
else:
    print("odd")
        
    
