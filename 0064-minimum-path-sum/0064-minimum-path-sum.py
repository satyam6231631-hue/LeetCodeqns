class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        def f(i,j):
            if i==m-1 and j==n-1:
                return grid[m-1][n-1]
            if i>=m or j>=n:
                return float("inf")
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=float("inf")
            ans=min(ans,grid[i][j]+f(i+1,j),grid[i][j]+f(i,j+1))
            dp[i][j]=ans
            return ans
        return f(0,0)

        