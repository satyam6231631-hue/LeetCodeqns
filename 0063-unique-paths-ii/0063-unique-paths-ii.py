class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]==1:
            return 0
        dp=[[-1]* (n+1) for _ in range(m+1)]
        def f(i,j):
            if (i,j)==(m-1,n-1):
                return 1
            if i>=m or j>=n:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=0
            ans=f(i+1,j)+f(i,j+1)
            dp[i][j]=ans
        
           
        
            return dp[i][j]
        return f(0,0)
                


            

     
        