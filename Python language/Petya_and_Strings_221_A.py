a=str(input())
b=str(input())
A=a.lower()
B=b.lower()
c=len(a)
for i in range(0,c):
    if ord(A[i]) > ord(B[i]):
        print(1)
        break
    if ord(A[i]) < ord(B[i]):
        print(-1)
        break
else:
    print(0)
