n,k,l,c,d,p,nl,np=map(int,input().split())
print(min(k*l//nl,c*d,p//np)//n)
"""n, k, l, c, d, p, nl, np = map(int, input().split())

# 计算每种资源可以支持的最大敬酒次数
total_drink = k * l
total_lime_slices = c * d
total_salt = p

# 每个朋友需要的资源量
drink_per_toast_per_person = n * nl
lime_slices_per_person = n
salt_per_toast_per_person = n * np

# 计算每种资源可以支持的最大敬酒次数
max_toasts_drink = total_drink // drink_per_toast_per_person
max_toasts_lime = total_lime_slices // lime_slices_per_person
max_toasts_salt = total_salt // salt_per_toast_per_person

# 每个朋友可以做的最大敬酒次数是三种资源中的最小值
max_toasts_per_friend = min(max_toasts_drink, max_toasts_lime, max_toasts_salt)

print(max_toasts_per_friend)"""
"""后一种方法避免多次//同时适时存储变量，减少变量调用，运行更快"""
