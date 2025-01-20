n=int(input())
trees=[]
for _ in range(n):
    x,h=map(int,input().split())
    trees.append([x,h])
if n==1 or n == 2:
    print(n)
else:
    num=2
    for i in  range(1,n-1):
        if trees[i][1]<trees[i][0]-trees[i-1][0]:
            num+=1
        elif trees[i][1]<trees[i+1][0]-trees[i][0]:
            num+=1
            trees[i][0]+=trees[i][1]
        else:
            continue
    print(num)



