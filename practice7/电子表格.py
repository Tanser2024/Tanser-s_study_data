# 定义字母到数字的映射
e = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ex = dict(zip(e, list(range(0, 27))))

def system1_to_2(data, excel):
    col = 0
    m = 0
    for i in range(len(data)):
        if data[i].isdigit():
            m = i
            break
    d = data[:m]
    row = int(data[m:])
    for i in range(len(d)):
        col += excel[d[-(i + 1)]] * (26 ** i)
    print(f"R{row}C{col}")

def system2_to_1(data, excel):
    row = int(data[1:data.index("C")])
    col = int(data[data.index("C") + 1:])
    string = ""
    while col > 0:
        col, remainder = divmod(col - 1, 26)
        string = e[remainder + 1] + string
    print(f"{string}{row}")

n = int(input())
for _ in range(n):
    da = input().strip()
    if da[0] == "R" and "C" in da and da[1] not in ex:
        system2_to_1(da, e)
    else:
        system1_to_2(da, ex)