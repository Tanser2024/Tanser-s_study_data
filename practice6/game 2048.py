def game2048(lst):
    nums=sorted([[i,lst.count(2**i)] for i in range(12)],key=lambda x:x[0])
    for i in range(11):
        nums[i+1][1]+=nums[i][1]//2
    if nums[11][1]>=1:
        return "Yes"
    else:
        return "No"
cases=int(input())
for _ in range(cases):
    n=int(input())
    l=list(map(int,input().split()))
    print(game2048(l))
