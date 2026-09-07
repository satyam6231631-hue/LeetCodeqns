class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        curr,ans=[],[]
        def f(i):
            if i==len(s):
                ans.append(" ".join(curr[::]))
                return
            for j in range(i,len(s)+1):
                if s[i:j] in wordDict:
                    curr.append(s[i:j])
                    f(j)
                    curr.pop()
        f(0)
        return ans
        