class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        from collections import deque

        vst=[False]*n
        prov=0
        def bfs(src):
            q=deque([src])
            vst[src]=True
            while q:
                node=q.popleft()
                for col in range(n):
                    if isConnected[node][col]==1 and not vst[col]:
                        bfs(col)




        for node  in range(n):
            if not vst[node]:
                prov+=1
                bfs(node)
        return prov

            
        