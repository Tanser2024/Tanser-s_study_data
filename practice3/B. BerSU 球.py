n=int(input())
boys=sorted(map(int,input().split()))
m=int(input())
girls=sorted(map(int,input().split()))
pairs=0
for i in boys:
    if i-1 in girls:
        pairs+=1
        girls.remove(i-1)
    elif i in girls:
        pairs += 1
        girls.remove(i )
    elif i+1 in girls:
        pairs += 1
        girls.remove(i+1)
print(pairs)
