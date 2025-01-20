


def spiralOrder(self, matrix):
    m, n = len(matrix), len(matrix[0])
    left,right,bottom,top=0,n,0,m
    results=[]
    while len(results)<n*m:
        for i in range(right):
            results.append(matrix[bottom][i])
        bottom+=1

        for i in range(bottom,top):
            results.append(matrix[i][right-1])
        right-=1

        for i in range(right-1,left-1,-1):
            results.append(matrix[top-1][i])
        top-=1

        for i in range(top-1,bottom-1,-1):
            results.append(matrix[i][left])
        left-=1
    return results
