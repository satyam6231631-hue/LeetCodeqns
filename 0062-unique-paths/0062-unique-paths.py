class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def f(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            right=f(i+1,j)
            down=f(i,j+1)
            dp[i][j]=right+down
            return dp[i][j]
        return f(0,0)

        