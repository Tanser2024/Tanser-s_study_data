m,n=map(int,input().split())
mat=[[[x] for x in list(input().split())] for _ in range(m)]
import sys
data=sys.stdin.readlines()


def check(x,y):
    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        tx,ty=x+dx,y+dy
        if 0<=tx<m and 0<=ty<n :
            if mat[x][y][1]==mat[tx][ty][1]:

                return True
    return False

from collections import defaultdict
dic=defaultdict(int)
def perfect_percent():
    total=n*m*4/10
    possible_num=0
    scores=sorted(list(dic.items()),reverse=True)
    for score , num in scores:
        possible_num+=num
        if possible_num>total:
            return possible_num-num

for i in range(m):
    for j in range(n):
        num=int(mat[i][j][0])
        score=sum(map(int,data[num].split()))
        dic[score]+=1
        mat[i][j].append(data[num].strip("\n"))

valid_num=0
for i in range(m):
    for j in range(n):
        if check(i,j):
            valid_num+=1

print(valid_num,perfect_percent())