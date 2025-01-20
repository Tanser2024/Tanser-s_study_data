n=int(input())
l=[]
for a in range(2,n+1):
    for d in range(2,a):
        for c in range(2,d+1):
            for b in range(2,c+1):
                if a**3==b**3+c**3+d**3:
                    l.append((a,b,c,d))
l.sort()
for a,b,c,d in l:
    print(f"Cube = {a}, Triple = ({b},{c},{d})")