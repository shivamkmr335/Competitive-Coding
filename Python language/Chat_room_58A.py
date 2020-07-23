a=str(input())
b=['h','e','l','l','o']
c=len(a)
counter=0
for i in range(0,c):
    if a[i]==b[counter]:
        counter=counter+1
        if counter==5:
            print("YES")
            break
else:
    print("NO")

    
    
