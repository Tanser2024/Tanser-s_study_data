n=int(input())
strings=[]
for _ in range(n):
    strings.append(list(input()))
o=[]
for i in range(50):
    if all(string[i]==strings[0][i] for string in strings):
        o.append(strings[0][i])
    else:
        break
print("".join(o))
