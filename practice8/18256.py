

target=int(input())
lst=sorted(list(map(int,input().split())))
i=0;j=len(lst)-1
old_sum=lst[i]+lst[j]
old_cha=abs(lst[i]+lst[j]-target)
while True:
    new_sum=lst[i]+lst[j]
    new_cha=abs(new_sum-target)
    if new_cha<old_cha:
        old_sum=new_sum
        old_cha=new_cha
    if new_cha==old_cha:
        old_sum=min(old_sum,new_sum)
    if new_sum>target:
        j-=1
    if new_sum<target:
        i+=1
    if i>=j or new_sum==target:
        break
print(old_sum)