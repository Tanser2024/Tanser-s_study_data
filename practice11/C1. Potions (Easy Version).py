n=int(input())
potions=list(map(int,input().split()))

rest_health=0
used_potions=[]
min_potions=float("inf")
for i in range(1,n+1):
    if rest_health+potions[i-1]>=0:

        rest_health+=potions[i-1]
        used_potions.append(potions[i-1])
        min_potions=min(min_potions,potions[i-1])

    else:
        if potions[i-1]>min_potions:
            ans= rest_health-min_potions+potions[i-1]
            if ans>=0:
                rest_health=ans
                used_potions.remove(min_potions)
                used_potions.append(potions[i-1])
                min_potions=min(used_potions)
print(len(used_potions))


