def next_lst(l):
    for i in range(len(l)-1,0,-1):
        if l[i]>l[i-1]:
            for j in range(len(l)-1,i-1,-1):
                if l[j]>l[i-1]:
                    l[i-1],l[j]=l[j],l[i-1]

                    l[i:]=reversed(l[i:])
                    return l
    return l[::]

n=int(input())
lst=list(map(int,input().split()))

outputs= [lst[:]]
lst=next_lst(lst)

while lst not in outputs:
    outputs.append(lst[:])
    lst=next_lst(lst)
outputs=sorted(outputs)
for line in outputs:
    print(*line)

