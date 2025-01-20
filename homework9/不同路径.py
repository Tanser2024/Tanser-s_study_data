def uniquePaths(self, m, n):
    def frac(x, y):
        if x==y:
            return 1
        s = x;
        s1 = 1
        for i in range(x - 1, y, -1):
            s *= i
        for j in range(1, x - y + 1):
            s1 *= j
        return s // s1

    print(frac(m + n - 2, n - 1))
uniquePaths(1,1,10)
