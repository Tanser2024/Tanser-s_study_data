num=0
lst0=[(6,0,0),(0,6,0),(0,0,6),(5,1,0),(5,0,1),(1,5,0),(0,5,1),(1,0,5),(0,1,5),(4,2,0),(4,0,2),(2,4,0),(0,4,2),(2,0,4),(0,2,4),(3,3,0),(3,0,3),(0,3,3),(3,2,1),(3,1,2),(2,3,1),(2,1,3),(1,3,2),(1,2,3),(2,2,2)]
lst=[(int(x),int(y),int(z)) for x,y,z in lst0]

for x0,y0,z0 in lst:
    for x1,y1,z1 in lst:
        for x2,y2,z2 in lst:
            for x3,y3,z3 in lst:
                if x0+x1+x2+x3==y0+y1+y2+y3==z0+z1+z2+z3==8:
                    num+=1
print(num)