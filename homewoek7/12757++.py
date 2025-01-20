# 定义英文数字对应的阿拉伯数字
english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty',
           'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million']
number = list(range(21)) + [30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000]
english_number = dict(zip(english, number))

# 获取用户输入的英文数字字符串
s = input().split()

num = 0
ans = 0
flag = 1

# 遍历输入的英文数字字符串
for i in range(len(s)):
    if s[i] == 'negative':
        flag *= -1
    elif s[i] == 'hundred':
        num *= 100
    elif s[i] == 'million' or s[i] == 'thousand':
        ans += num * english_number[s[i]]
        num = 0
    else:
        num += english_number[s[i]]

# 输出最终结果
print(flag * ans)