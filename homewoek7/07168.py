
num=int(input())
patients=[list(map(str,input().split())) for _ in range(num)]
olds=sorted([x for x in patients if int(x[1])>=60],key = lambda x:int(x[1]),reverse=True)
others=[x for x in patients if x not in olds]
all_patients=olds+others
for i in all_patients:
    print(i[0])