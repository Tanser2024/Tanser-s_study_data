def is_valid(row,col,board):
    if any(abs(col-i)==abs(row-j) for j,i in enumerate(board)) or col in board:
        return False
    return True
def solve_queens(n):
    stack=[(0,tuple())]
    solutions=[]
    while stack:
        row,cols=stack.pop()
        if row==8:
            solutions.append(cols)
        else:
            for col in range(1,n+1):
                if is_valid(row,col,cols):
                    stack.append((row+1,cols+(col,)))
    return solutions
n=int(input())
s = sorted(solve_queens(8))
for i in range(n):
    print("".join(map(str,s[int(input())-1])))
