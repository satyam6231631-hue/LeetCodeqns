class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for ch in s:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1
        
        arr=list(dic.items())
        arr.sort(key=lambda x:x[1])
        arr=arr[::-1]
       
        s=""
        for i in range(len(arr)):
            s+=(arr[i][0]*arr[i][1])
        return s
    
        