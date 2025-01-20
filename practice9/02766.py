import sys
n=int(input())
lst=list(sys.stdin.read().strip().split())
lst=[[int(lst[i+n*j] )for i in range(n)] for j in range(n)]
def kadane(lis):
    max_end_here=max_so_far=0
    for i in lis:
        max_end_here=max(max_end_here+i,i)
        max_so_far=max(max_end_here,max_so_far)
    return max_so_far
def max_matrix(mat):
    max_sum=-float("inf")
    for left in range(len(mat[0])):
        temp=[0]*len(mat)
        for right in range(left,len(mat[0])):
            for row in range(len(mat)):
                temp[row]+=mat[row][right]
            max_sum=max(max_sum,kadane(temp))
    return max_sum
print(max_matrix(lst))