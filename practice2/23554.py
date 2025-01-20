n=int(input())
lst=input().split()
self=[]
for i in range(1,n+1):
    if str(i) not in lst:
        self.append(str(i))
others=[int(x) for x in lst if int(x)>n]
a=sorted(others)#数字和字符都可以按大小排，结果截然不同
print(" ".join(self))
b=map(str,a)
print(" ".join(map(str,a)))#只有字符可以拼接，整数不行


