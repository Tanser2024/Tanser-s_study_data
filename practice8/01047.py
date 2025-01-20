import sys
def is_valid(num,length):

    if int(num)*length>10**length-1:
        return False
    for i in range(1,length+1):
        new_num=""
        up_num = 0
        for j in range(length-1,-1,-1):
            if up_num:
                the_num=str(int(num[j])*i+up_num)
                up_num=0
            else:
                the_num=str(int(num[j])*i)
            if len(the_num)>1:
                up_num=int(the_num[:-1])
            new_num=the_num[-1]+new_num

        if all(new_num[k:]+new_num[:k]!=num for k in range(length)):
            return False
    return True
nums=sys.stdin.readlines()
for line in nums:
    line=line.strip()
    if is_valid(line,len(line)):
        print(f"{line} is cyclic")
    else:
        print(f"{line} is not cyclic")

