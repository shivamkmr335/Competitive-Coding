a=str(input())
b=list(a)
cap=0
sml=0
for i in b:
     if ord(i)>64 and ord(i)<91:
          cap=cap+1
     else:
          sml=sml+1
if cap>sml:
     print(a.upper())
else:
     print(a.lower())

     
