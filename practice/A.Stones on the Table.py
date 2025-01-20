"""n=int(input())
a=input()
b=[]
stones_colour=list(a)
i=0
while True:

    while stones_colour[i]==stones_colour[i+1]:
        b.append(stones_colour[i])
    i+=1
    if not stones_colour[i+1]:
        break
print(len(b))
以上这段代码存在以下问题：
索引越界：在 while stones_colour[i] == stones_colour[i + 1] 中，当 i 达到 len(stones_colour) - 1 时，i + 1 会超出列表的范围。
循环条件：if not stones_colour[i + 1] 这个条件不正确，因为即使 stones_colour[i + 1] 存在且非空字符串，这个条件也会为 False。
逻辑错误：b.append(stones_colour[i]) 只在颜色相同时添加元素，但没有处理颜色不同的情况。
"""
n=int(input())
string=input()
remove_count=0
for i in range(1,n):
    if string[i]==string[i-1]:
        remove_count+=1
print(remove_count)
"""
22 23行的处理保证了string[i-1]有意义
注意 字符串 string[i]可直接返回对应单个字符
"""






