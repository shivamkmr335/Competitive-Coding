n=int(input())
enter=0
leave=0
current=0
max=0
for i in range(0,n):
    leave,enter=list(map(int,input().split(" ")))
    current=current-leave+enter
    if current >= max:
        max=current
print(max)
        
