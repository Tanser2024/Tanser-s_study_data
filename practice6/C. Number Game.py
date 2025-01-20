def most_k(nums,n,k):
    if len(nums)==2:
        return k+1
    else:
        nums=[x for x in nums if x <=k]