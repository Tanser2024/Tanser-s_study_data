
string=list(input().split())
while len(string)>2:

    for i in range(len(string)):
        if string[i] in "+-*/" and string[i+1] not in "+-*/ " and string[i+2] not in "+-*/ ":
            a=string[i+1]+string[i]+string[i+2]
            string[i+1]=str(eval(a))
            string[i]=string[i+2]=" "
    string=[string[i] for i in range(len(string)) if string[i]!=" "]

print("%.6f"%float(string[0]))


"""# http://cs101.openjudge.cn/practice/02694/
s = input().split()
def cal():
    cur = s.pop(0)
    if cur in "+-*/":
        return str(eval(cal() + cur + cal()))
    else:
        return cur
print("%.6f" % float(cal()))"""