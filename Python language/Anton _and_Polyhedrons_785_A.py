a=int(input())
count=0
for i in range(0,a):
     b=str(input())
     if b=="Icosahedron":
          count=count+20
     if b=="Cube":
          count=count+6
     if b=="Tetrahedron":
          count=count+4
     if b=="Dodecahedron":
          count=count+12
     if b=="Octahedron":
          count=count+8
print(count)
