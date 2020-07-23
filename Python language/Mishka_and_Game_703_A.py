i=int(input())
girl=0
boy=0
for i in range(0,i):
    b=list(map(int,input().split(" ")))
    if b[0] > b[1]:
        girl=girl+1
    if b[0] < b[1]:
        boy=boy+1
if girl>boy:
    print("Mishka")
elif boy>girl:
    print("Chris")
elif boy==girl:
    print("Friendship is magic!^^")
