class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["."]*n for _ in range (n)]
        def isSafe(row,col):
            i=row
            while(i>=0):
                if board[i][col]=="Q":
                    return False
                i-=1
            i,j=row,col
            while(i>=0 and j>=0):
                if board[i][j]=="Q":
                    return False
                i-=1
                j-=1
            i,j=row,col
            while(i>=0 and j<n):
                if board[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True        


        def fn(row):
            if row==n:
                temp=[]
                for eachrow in board:
                    temp.append("".join(eachrow))
                ans.append(temp)
                return
            for col in range(n):
                if isSafe(row,col):
                    board[row][col]="Q"
                    fn(row+1)
                    board[row][col]="."
        fn(0)
        return ans
        

        