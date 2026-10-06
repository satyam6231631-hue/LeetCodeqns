class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)

        vst=[False]*n
        prov=0
        def dfs(node):
            vst[node]=True 
            for col in range(n):
                if isConnected[node][col]==1 and not vst[col]:
                    dfs(col)
                    

        for node  in range(n):
            if not vst[node]:
                prov+=1
                dfs(node)
        return prov

            
        