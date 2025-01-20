"""name=input()
a=list(name)#该方法可直接江输入的字符串转换为单个字符构成的列表
b=set(a)
print(len(b))"""
name=input()
num=len(set(i for i in name))
if num%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")