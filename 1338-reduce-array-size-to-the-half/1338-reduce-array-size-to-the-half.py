class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        n=len(arr)//2
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        arr=list(dic.items())
        if len(arr)==1:
            return 1
        c=0
        
        arr.sort(key=lambda x:x[1],reverse=True)
        print(arr)
        removed_elements=0
        
        for ch,freq in arr:
            removed_elements+=freq
            c+=1
            if removed_elements>=n:
                break
        return c
                





      
     

        
        
        