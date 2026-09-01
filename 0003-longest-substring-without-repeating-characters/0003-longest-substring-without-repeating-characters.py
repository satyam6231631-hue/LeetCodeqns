class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        dic={}
        ans=0
        while(right<len(s)):
            if s[right] not in dic:
                
                dic[s[right]]=right
                right+=1
            else:
                left=max(left,dic[s[right]]+1)
                dic[s[right]]=right
                right+=1
            ans=max(ans,right-left)
        return ans

                


        

        
       


        